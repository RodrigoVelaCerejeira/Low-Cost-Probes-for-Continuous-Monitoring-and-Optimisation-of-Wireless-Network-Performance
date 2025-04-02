import time
import subprocess
import mariadb
import requests
import netifaces

# Função para obter o IP local
def get_local_ip():
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
        print(f"Erro ao obter IP local: {e}")
        return "Erro"

# Função para obter o IP externo
def get_external_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip", "Desconhecido")
    except requests.RequestException as e:
        print(f"Erro ao obter IP externo: {e}")
        return "Erro"

# Função para medir latência (ping) e perda de pacotes
def medir_ping(destino="8.8.8.8"):
    try:
        resultado = subprocess.run(["ping", "-c", "4", destino], capture_output=True, text=True)
        latencia = None
        perda_pacotes = None
        rtt_min = None
        rtt_avg = None
        rtt_max = None
        rtt_mdev = None

        # Percorrer a saída do ping
        for linha in resultado.stdout.split("\n"):
            if "avg" in linha:
                latencia = float(linha.split("/")[-3].replace(' ms', ''))  # Remover 'ms' antes de converter
            if "packet loss" in linha:
                partes = linha.split(",")
                perda_pacotes = float(partes[2].split()[0].replace('%', ''))
            if "rtt min/avg/max/mdev" in linha:
                rtt_values = linha.split("=")[-1].strip().split("/")
                rtt_min = float(rtt_values[0].replace(' ms', ''))  # Remover 'ms' antes de converter
                rtt_avg = float(rtt_values[1].replace(' ms', ''))  # Remover 'ms' antes de converter
                rtt_max = float(rtt_values[2].replace(' ms', ''))  # Remover 'ms' antes de converter
                rtt_mdev = float(rtt_values[3].replace(' ms', ''))  # Remover 'ms' antes de converter

        return latencia, perda_pacotes, rtt_min, rtt_avg, rtt_max, rtt_mdev

    except Exception as e:
        print(f"Erro ao medir latência: {e}")
        return None, None, None, None, None, None

# Função para medir velocidade de internet
def medir_velocidade():
    try:
        resultado = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
        download = upload = None
        for linha in resultado.stdout.split("\n"):
            if "Download" in linha:
                download = float(linha.split()[1])
            if "Upload" in linha:
                upload = float(linha.split()[1])
        return download, upload
    except Exception as e:
        print(f"Erro ao medir velocidade: {e}")
        return None, None

# Função para conectar à base de dados local
def conectar_db():
    try:
        conn = mariadb.connect(
            host="localhost",
            user="monitor",
            password="senha_segura",
            database="monitoramento"
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar à base de dados: {e}")
        return None

# Função para conectar à base de dados central
def conectar_central():
    try:
        conn = mariadb.connect(
            host="100.68.11.69",  # Endereço do servidor central
            user="rodrigo",        # Verifique o nome correto do usuário
            password="senha_segura",  # Senha do usuário 'rodrigo'
            database="central_monitoramento"
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB central: {e}")
        return None

# Função para obter o mac_address da interface de rede
def get_mac_address():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'wlan0' or interface == 'eth0':  # Verifica as interfaces de rede
            mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            return mac
    return "Desconhecido"

import subprocess

# Função para verificar se o Raspberry Pi está conectado à rede
def is_connected(ip):
    try:
        # Executar o comando ping e verificar a resposta
        result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True  # Conectado
        else:
            return False  # Não conectado
    except Exception as e:
        print(f"Erro ao verificar conectividade com {ip}: {e}")
        return False

def inserir_dados(latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdev):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            ip_local = get_local_ip()
            ip_externo = get_external_ip()

            # Consultar todos os Raspberry Pis com status 'ativo'
            cursor.execute("SELECT mac_address, raspberrypi_id, ip_local FROM raspberrypis WHERE status = 'ativo'")
            ativos = cursor.fetchall()

            for mac_address, raspberrypi_id, ip in ativos:
                # Verificar se o Raspberry Pi está realmente conectado à rede
                if is_connected(ip):
                    # Se estiver conectado, coletemos os dados
                    print(f"Coletando dados para Raspberry Pi com ID {raspberrypi_id} (MAC: {mac_address})")

                    cursor.execute("""
                        INSERT INTO dados_rede (raspberrypi_id, timestamp, ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev)
                        VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (raspberrypi_id, ip_local, ip_externo, latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdev))

                    conn.commit()
                else:
                    print(f"Raspberry Pi com ID {raspberrypi_id} (MAC: {mac_address}) não está conectado à rede. Ignorando coleta de dados.")

        except mariadb.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
    else:
        print("Erro ao conectar à base de dados para inserção de dados.")

# Função para coletar dados continuamente
def coletar_dados():
    while True:
        latencia, perda_pacotes, rtt_min, rtt_avg, rtt_max, rtt_mdev = medir_ping()  # Chama a função medir_ping
        download, upload = medir_velocidade()

        # Chama a função inserir_dados com todos os parâmetros necessários
        inserir_dados(latencia, perda_pacotes, download, upload, rtt_min, rtt_avg, rtt_max, rtt_mdev)

        time.sleep(60)

# Executar os dados
if __name__ == "__main__":
    coletar_dados()
