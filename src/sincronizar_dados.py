import os
from logging import error
import mariadb
import subprocess


def get_default_interface():
    """Funcao para descobrir a interface utilizada pelo dispositivo

    Returns:
        Retorna o nome da interface
    """
    # Get the name of the default interface (used for default route)
    result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if line.startswith('default'):
            return line.split()[4]
    return None


def get_mac_address(interface: str):
    """Retorna o mac address da interface do dispositivo

    Args:
        interface (string): interface a descrever o mac address

    Returns:
        retorna o mac address da interface
    """
    try:
        with open(f'/sys/class/net/{interface}/address') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_location():
    return os.getenv("LOCATION")


def conectar_local():
    """Funcao para conectar a base de dados local

    Returns:
        Conn para a base de dados local
    """
    try:
        conn = mariadb.connect(
            host="localhost",  # Banco de dados local
            user="monitor",
            password="senha_segura",
            database="monitoramento"
        )
        return conn
    except mariadb.Error as e:
        error(f"Erro ao conectar ao MariaDB local: {e}")
        return None


def conectar_central():
    """Funcao para conectar a base de dados central

    Returns:
        Conn para a base de dados central
    """
    try:
        conn = mariadb.connect(
            host="192.92.147.85",  # IP do banco de dados central
            user="monitor",
            password="senha_segura",
            database="central_monitoramento"
        )
        print("Conexão com o banco de dados central bem-sucedida!")
        return conn
    except mariadb.Error as e:
        error(f"Erro ao conectar ao MariaDB central: {e}")
        return None


def inserir_raspberrypi_central(conn_central, mac_address):
    """Funcao para adicionar o dispositivo a tabela de dispositivos da base de dados central

    Args:
        conn_central (Conn): Conn para a base de dados central
        mac_address (str): mac address do dispositivo

    Returns:
        Id do dispositivo guardado na base de dados local
    """
    cursor_central = conn_central.cursor()
    # Verifica se o raspberrypi_id já existe na tabela central
    cursor_central.execute(
        "SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
    result = cursor_central.fetchone()
    location = get_location()

    # Se o Raspberry Pi não existir, insira-o
    if not result:
        print(f"Inserindo Raspberry Pi {mac_address} na tabela central.")
        cursor_central.execute("""
            INSERT INTO raspberrypis (mac_address, localizacao)
            VALUES (?, ?)
        """, (mac_address, location))
        conn_central.commit()
        print(f"Raspberry Pi {mac_address} inserido com sucesso!")
    else:
        result = result[0]
        cursor_central.execute("""
            UPDATE raspberrypis
            SET
            ultimo_registro = CURRENT_TIMESTAMP,
            localizacao = ?
            WHERE id = ?
        """, (location, result))
        conn_central.commit()

    # Retorna o id do Raspberry Pi inserido ou existente
    cursor_central.execute(
        "SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
    raspberrypi_id = cursor_central.fetchone()[0]
    return raspberrypi_id

# Função para sincronizar dados da tabela dados_rede


def sincronizar_dados(mac_address):
    """Funcao para sincronizar a base de dados local com a base de dados central

    Args:
        mac_address (str): mac address do dispositivo
    """
    conn_local = conectar_local()
    conn_central = conectar_central()

    if conn_local and conn_central:
        try:
            cursor_local = conn_local.cursor()
            cursor_central = conn_central.cursor()

            # Selecionar os dados da tabela dados_rede na base de dados local
            cursor_local.execute(
                "SELECT timestamp, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev, num_aps, id FROM dados_rede WHERE synch = FALSE")
            dados_rede = cursor_local.fetchall()
            raspberrypi_id_central = inserir_raspberrypi_central(conn_central, mac_address)

            for dado in dados_rede:
                timestamp = dado[0]
                latencia = dado[1]  # Latência

                perda_pacotes = dado[2]  # Perda de pacotes
                download = dado[3]  # Download
                upload = dado[4]  # Upload
                rtt_min = dado[5]  # RTT Mínimo
                rtt_avg = dado[6]  # RTT Médio
                rtt_max = dado[7]  # RTT Máximo
                rtt_mdev = dado[8]  # RTT Mdev
                num_aps = dado[9]
                id = dado[10]

                # Inserir os dados na tabela dados_rede no banco de dados central
                cursor_central.execute("""
                    INSERT INTO dados_rede (timestamp, latencia_ms, perda_pacotes, download_mbps, upload_mbps, raspberrypi_id, rtt_min, rtt_avg, rtt_max, rtt_mdev, num_aps)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (timestamp, latencia, perda_pacotes, download, upload, raspberrypi_id_central, rtt_min, rtt_avg, rtt_max, rtt_mdev, num_aps))

                cursor_local.execute("""
                    UPDATE dados_rede
                    SET synch = TRUE
                    WHERE id = ?
                """, (id,))

                conn_central.commit()
                conn_local.commit()

            cursor_local.execute( "SELECT timestamp, ssid, bssid, rate, sig from aps")
            dados_aps = cursor_local.fetchall()

            cursor_central.execute("DELETE FROM all_aps WHERE raspberrypi_id = ?", (raspberrypi_id_central,))
            for dado in dados_aps:
                timestamp = dado[0]
                ssid = dado[1]
                bssid = dado[2]
                rate = dado[3]
                sig = dado[4]
                cursor_central.execute("""
                    INSERT INTO all_aps (timestamp, raspberrypi_id, ssid, bssid, rate, sig)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """, (timestamp, raspberrypi_id_central, ssid, bssid, rate, sig))
                conn_central.commit()


            print("Dados sincronizados com sucesso!")

        except mariadb.Error as e:
            error(f"Erro ao sincronizar dados: {e}")
        finally:
            conn_local.close()
            conn_central.close()
    else:
        error("Erro ao conectar às bases de dados para sincronização.")


# Executar a sincronização
if __name__ == "__main__":
    iface = get_default_interface()
    if iface:
        mac_address = get_mac_address(iface)
    else:
        raise Exception("Erro a ler o mac address do raspberry")

    raspberry_id = sincronizar_dados(mac_address)

