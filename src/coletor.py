from logging import error
import time
import subprocess
import mariadb # type: ignore
import requests
import netifaces

def get_local_ip():
    """Funcao para descobrir o ip local do dispositivo

    Returns:
        O ip local
    """
    try:
        interfaces = netifaces.interfaces()

        for interface in interfaces:
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                ip_info = netifaces.ifaddresses(interface)[netifaces.AF_INET]
                for info in ip_info:
                    ip_local = info['addr']
                    return ip_local

        return "Desconhecido"

    except Exception as e:
        error(f"Erro ao obter IP local: {e}")
        return None



def get_external_ip():
    """Funcao para descobrir o ip global do dispositivo

    Returns:
        Retorna o ip global do dispositivo
    """
    try:
        response = requests.get(
            "https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip", "Desconhecido")
    except requests.RequestException as e:
        error(f"Erro ao obter IP externo: {e}")
        return None



def medir_ping(destino="8.8.8.8"):
    """Funcao para medir alguns parametros a inserir na base de dados, com base num ping

    Args:
        destino (str): destino a fazer o ping

    Returns:
        Retorna alguns valores a inserir na base de dados
    """
    try:
        resultado = subprocess.run(
            ["ping", "-c", "4", destino], capture_output=True, text=True)
        latencia = None
        perda_pacotes = None
        rtt_min = None
        rtt_avg = None
        rtt_max = None
        rtt_mdev = None

        for linha in resultado.stdout.split("\n"):
            if "avg" in linha:
                latencia = float(linha.split("/")[-3].replace(' ms', ''))
            if "packet loss" in linha:
                partes = linha.split(",")
                perda_pacotes = float(partes[2].split()[0].replace('%', ''))
            if "rtt min/avg/max/mdev" in linha:
                rtt_values = linha.split("=")[-1].strip().split("/")
                rtt_min = float(rtt_values[0].replace(' ms', ''))
                rtt_avg = float(rtt_values[1].replace(' ms', ''))
                rtt_max = float(rtt_values[2].replace(' ms', ''))
                rtt_mdev = float(rtt_values[3].replace(' ms', ''))

        return latencia, perda_pacotes, rtt_min, rtt_avg, rtt_max, rtt_mdev

    except Exception as e:
        error(f"Erro ao medir latência: {e}")
        return None, None, None, None, None, None



def medir_velocidade():
    """Funcao para medir alguns valores a inserir na base de dados, com base no comando speedtest-cli

    Returns:
        Retorna alguns valores a inserir na base de dados
    """
    try:
        resultado = subprocess.run(
            ["speedtest-cli", "--simple"], capture_output=True, text=True)
        download = upload = None
        for linha in resultado.stdout.split("\n"):
            if "Download" in linha:
                download = float(linha.split()[1])
            if "Upload" in linha:
                upload = float(linha.split()[1])
        return download, upload
    except Exception as e:
        error(f"Erro ao medir velocidade: {e}")
        return None, None



def conectar_db():
    """Funcao para conectar a base de dados local

    Returns:
        Conn para a base de dados local
    """
    try:
        conn = mariadb.connect(
            host="localhost",
            user="monitor",
            password="senha_segura",
            database="monitoramento"
        )
        return conn
    except mariadb.Error as e:
        error(f"Erro ao conectar à base de dados: {e}")
        return None


def inserir_dados(latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdev):
    """Funcao para inserir os valores na base de dados

    Args:
        latencia (str): latencia medida
        perda_pacotes (str): perda de pacotes medida
        download (str): download medido
        upload (str): upload medido
        rtt_min (str): rtt_min medido
        rtt_avg (str): rtt_avg medido
        rtt_max (str): rtt_max medido
        rtt_mdev (str): rtt_mdev medido
    """
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            ip_local = get_local_ip()
            ip_externo = get_external_ip()

                # Se estiver conectado, coletemos os dados

            cursor.execute("""
                INSERT INTO dados_rede (ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (ip_local, ip_externo, latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdev))

            conn.commit()

        except mariadb.Error as e:
            error(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
    else:
        error("Erro ao conectar à base de dados para inserção de dados.")





# Executar os dados
while True:
    if __name__ == "__main__":
        print("A comecar a ler os valores")
        latencia, perda_pacotes, rtt_min, rtt_avg, rtt_max, rtt_mdev = medir_ping()
        download, upload = medir_velocidade()
        print("Acabou de ler os valores")

        print("A inserir dados na tabela local")
        inserir_dados(latencia, perda_pacotes, download, upload,
                      rtt_min, rtt_avg, rtt_max, rtt_mdev)
        print("Acabou de inserir na tabela local")

        time.sleep(300)


# Após a coleta de dados, chame o script de sincronização
def sincronizar_com_central():
    """Função para chamar o script de sincronização para a base de dados central"""
    try:
        subprocess.run(['python3', '/home/cerejeira/PIC/src/sincronizar_dados.py'], check=True)
        print("Sincronização com a base de dados central concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao sincronizar com a base de dados central: {e}")

# Chamar a função de sincronização após a coleta de dados
sincronizar_com_central()
