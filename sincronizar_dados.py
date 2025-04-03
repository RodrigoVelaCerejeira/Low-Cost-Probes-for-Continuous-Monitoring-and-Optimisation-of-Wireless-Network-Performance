import mariadb

# Função para conectar à base de dados local
def conectar_local():
    try:
        conn = mariadb.connect(
            host="localhost",  # Banco de dados local
            user="monitor",
            password="senha_segura",
            database="monitoramento"
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB local: {e}")
        return None

# Função para conectar à base de dados central
def conectar_central():
    try:
        conn = mariadb.connect(
            host="100.68.11.69",  # IP do banco de dados central
            user="rodrigo",
            password="senha_segura",
            database="central_monitoramento"
        )
        print("Conexão com o banco de dados central bem-sucedida!")
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB central: {e}")
        return None

# Função para inserir Raspberry Pi na tabela central, se não existir
def inserir_raspberrypi_central(conn_central, mac_address, ip_local, ip_externo):
    cursor_central = conn_central.cursor()
    # Verifica se o raspberrypi_id já existe na tabela central
    cursor_central.execute("SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
    result = cursor_central.fetchone()

    # Se o Raspberry Pi não existir, insira-o
    if not result:
        print(f"Inserindo Raspberry Pi {mac_address} na tabela central.")
        cursor_central.execute("""
            INSERT INTO raspberrypis (mac_address, ip_local, ip_externo, status)
            VALUES (?, ?, ?, ?)
        """, (mac_address, ip_local, ip_externo, 'ativo'))
        conn_central.commit()
        print(f"Raspberry Pi {mac_address} inserido com sucesso!")
    else:
        print(f"Raspberry Pi {mac_address} já existe na tabela central.")
    
    # Retorna o id do Raspberry Pi inserido ou existente
    cursor_central.execute("SELECT id FROM raspberrypis WHERE mac_address = ?", (mac_address,))
    raspberrypi_id = cursor_central.fetchone()[0]
    return raspberrypi_id

# Função para sincronizar dados da tabela dados_rede
def sincronizar_dados():
    conn_local = conectar_local()
    conn_central = conectar_central()

    if conn_local and conn_central:
        try:
            cursor_local = conn_local.cursor()
            cursor_central = conn_central.cursor()

            # Selecionar os dados da tabela dados_rede na base de dados local
            cursor_local.execute("SELECT ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, rtt_min, rtt_avg, rtt_max, rtt_mdev, raspberrypi_id FROM dados_rede")
            dados = cursor_local.fetchall()

            for dado in dados:
                raspberrypi_id = dado[10]  # Raspberry Pi ID da tabela local
                ip_local = dado[0]  # IP Local
                ip_externo = dado[1]  # IP Externo
                latencia = dado[2]  # Latência
                perda_pacotes = dado[3]  # Perda de pacotes
                download = dado[4]  # Download
                upload = dado[5]  # Upload
                rtt_min = dado[6]  # RTT Mínimo
                rtt_avg = dado[7]  # RTT Médio
                rtt_max = dado[8]  # RTT Máximo
                rtt_mdev = dado[9]  # RTT Mdev

                # Usar raspberrypi_id para pegar o mac_address da tabela local
                cursor_local.execute("SELECT mac_address FROM raspberrypis WHERE id = ?", (raspberrypi_id,))
                mac_address_result = cursor_local.fetchone()
                
                if mac_address_result:
                    mac_address = mac_address_result[0]  # O mac_address está na primeira coluna
                else:
                    print(f"Erro: Raspberry Pi com ID {raspberrypi_id} não encontrado na tabela local.")
                    continue  # Pula para o próximo Raspberry Pi

                # Inserir o Raspberry Pi na tabela central, se necessário
                raspberrypi_id_central = inserir_raspberrypi_central(conn_central, mac_address, ip_local, ip_externo)

                # Inserir os dados na tabela dados_rede no banco de dados central
                cursor_central.execute("""
                    INSERT INTO dados_rede (ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, raspberrypi_id, rtt_min, rtt_avg, rtt_max, rtt_mdev)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (ip_local, ip_externo, latencia, perda_pacotes, download, upload, raspberrypi_id_central, rtt_min, rtt_avg, rtt_max, rtt_mdev))

                conn_central.commit()

            print("Dados sincronizados com sucesso!")

        except mariadb.Error as e:
            print(f"Erro ao sincronizar dados: {e}")
        finally:
            conn_local.close()
            conn_central.close()
    else:
        print("Erro ao conectar às bases de dados para sincronização.")

# Executar a sincronização
sincronizar_dados()
