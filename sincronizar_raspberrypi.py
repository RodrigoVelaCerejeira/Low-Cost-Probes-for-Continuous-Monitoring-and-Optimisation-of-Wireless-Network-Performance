import mariadb

# Função para conectar à base de dados local
def conectar_local():
    try:
        conn = mariadb.connect(
            host="localhost", #IP REAL DO SERVIDOR CENTRAL (ATENÇAO)
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
            host="100.68.11.69",  # Substitua pelo IP da base central
            user="rodrigo",
            password="senha_segura",
            database="central_monitoramento"
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB central: {e}")
        return None

# Função para sincronizar dados da tabela dados_rede
def sincronizar_dados():
    conn_local = conectar_local()
    conn_central = conectar_central()

    if conn_local and conn_central:
        try:
            cursor_local = conn_local.cursor()
            cursor_central = conn_central.cursor()

            # Selecionar os dados da tabela dados_rede na base de dados local
            cursor_local.execute("SELECT id, ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, raspberrypi_id FROM dados_rede")
            dados = cursor_local.fetchall()

            for dado in dados:
                # Verificar se o Raspberry Pi já existe na tabela central, se não, inserir
                raspberrypi_id = dado[7]  # Raspberry Pi ID da tabela local
                cursor_central.execute("SELECT id FROM raspberrypis WHERE id = ?", (raspberrypi_id,))
                result = cursor_central.fetchone()

                if result:
                    # Se o Raspberry Pi já existe, insira os dados de rede na tabela dados_rede
                    cursor_central.execute("""
                        INSERT INTO dados_rede (ip_local, ip_externo, latencia_ms, perda_pacotes, download_mbps, upload_mbps, raspberrypi_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, dado[1:8])  # Inserir dados de índice 1 a 7 (sem o id da tabela dados_rede)

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
