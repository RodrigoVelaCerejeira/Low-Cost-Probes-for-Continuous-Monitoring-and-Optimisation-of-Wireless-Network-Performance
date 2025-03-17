import time
import subprocess
import mariadb
import requests

# 🖥️ Função para obter o IP local


def get_local_ip():
    try:
        ip_list = subprocess.check_output(
            "hostname -I", shell=True).decode().strip().split()
        for ip in ip_list:
            if ip.startswith("192.168."):
                return ip
        return "Desconhecido"
    except Exception as e:
        print(f"Erro ao obter IP local: {e}")
        return "Erro"

# 🌍 Função para obter o IP externo


def get_external_ip():
    try:
        response = requests.get(
            "https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip", "Desconhecido")
    except requests.RequestException as e:
        print(f"Erro ao obter IP externo: {e}")
        return "Erro"

# 📶 Função para medir latência (ping)


def medir_ping(destino="8.8.8.8"):
    try:
        resultado = subprocess.run(
            ["ping", "-c", "4", destino], capture_output=True, text=True)
        for linha in resultado.stdout.split("\n"):
            if "avg" in linha:
                # Pega a média (avg) do ping
                return float(linha.split("/")[-3])
        return None
    except Exception as e:
        print(f"Erro ao medir latência: {e}")
        return None

# 🚀 Função para medir velocidade de internet


def medir_velocidade():
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
        print(f"Erro ao medir velocidade: {e}")
        return None, None

# 🔗 Função para conectar aa base de dados ariaDB


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
        print(f"Erro ao conectar a base de dados: {e}")
        return None

# 📊 Função para inserir os dados nnabase de dados


def inserir_dados(latencia, perda_pacotes, download, upload):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            ip_local = get_local_ip()
            ip_externo = get_external_ip()

            cursor.execute("""
                INSERT INTO dados_rede (ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (ip_local, ip_externo, latencia, perda_pacotes, download, upload))

            conn.commit()
            print("Dados inseridos com sucesso!")
        except mariadb.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
    else:
        print("Erro ao conectar a base de dados para inserção de dados.")

# 🔄 Loop para coleta contínua


def coletar_dados():
    while True:
        print("Adreunir ados da rede...")
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
    coletar_dados()
