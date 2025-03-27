import time
import subprocess
import mariadb
import requests
import netifaces

# 🖥️ Função para obter o IP local
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

# 🌍 Função para obter o IP externo
def get_external_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip", "Desconhecido")
    except requests.RequestException as e:
        print(f"Erro ao obter IP externo: {e}")
        return "Erro"

# 📶 Função para medir latência (ping)
def medir_ping(destino="8.8.8.8"):
    try:
        resultado = subprocess.run(["ping", "-c", "4", destino], capture_output=True, text=True)
        for linha in resultado.stdout.split("\n"):
            if "avg" in linha:
                return float(linha.split("/")[-3])
        return None
    except Exception as e:
        print(f"Erro ao medir latência: {e}")
        return None

# 🚀 Função para medir velocidade de internet
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

# 🔗 Função para conectar à base de dados MariaDB
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

def inserir_dados(latencia, perda_pacotes, download, upload):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            ip_local = get_local_ip()
            ip_externo = get_external_ip()
            mac_address = get_mac_address()  # Obter o mac_address do Raspberry Pi

            # Verificar se o raspberrypi já existe na base de dados
            cursor.execute("SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
            result = cursor.fetchone()

            if result:
                raspberrypi_id = result[0]  # Se encontrado, usar o ID existente
            else:
                print(f"⚠️ MAC {mac_address} não encontrado na base de dados. Inserindo agora...")
                # Inserir o mac_address, ip_local e ip_externo na tabela raspberrypis
                cursor.execute("""
                    INSERT INTO raspberrypis (mac_address, ip_local, ip_externo, status)
                    VALUES (?, ?, ?, ?)
                """, (mac_address, ip_local, ip_externo, 'ativo'))

                # Confirmar a inserção e obter o novo ID
                conn.commit()
                cursor.execute("SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
                raspberrypi_id = cursor.fetchone()[0]
                print(f"MAC {mac_address} inserido com sucesso! ID: {raspberrypi_id}")

            # Inserir os dados na tabela dados_rede
            cursor.execute("""
                INSERT INTO dados_rede (ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, raspberrypi_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (ip_local, ip_externo, latencia, perda_pacotes, download, upload, raspberrypi_id))

            conn.commit()
            print("Dados inseridos com sucesso!")

        except mariadb.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
    else:
        print("Erro ao conectar à base de dados para inserção de dados.")

# 🔄 Loop para coleta contínua

import netifaces
import uuid

# Função para obter o mac_address da interface de rede
def get_mac_address():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'wlan0' or interface == 'eth0':  # Verifica as interfaces de rede
            mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            return mac
    return "Desconhecido"


def coletar_dados():
    while True:
        print("A reunir dados da rede...")

        latencia = medir_ping()
        perda_pacotes = 0  # Podemos adicionar um cálculo para isso depois
        download, upload = medir_velocidade()

        print(f"""
        📍 IP Local: {get_local_ip()}
        🌍 IP Externo: {get_external_ip()}
           Latência: {latencia} ms
        📉 Perda de Pacotes: {perda_pacotes}%
           Download: {download} Mbps
           Upload: {upload} Mbps
        """)

        inserir_dados(latencia, perda_pacotes, download, upload)

        print("A aguardar 60 segundos para nova coleta...")
        time.sleep(60)

# Executar a coleta de dados
if __name__ == "__main__":
    coletar_dados()
