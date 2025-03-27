import mariadb

# Função para conectar à base de dados central
def conectar_central():
    try:
        conn = mariadb.connect(
            host="100.68.11.69",  # IP do servidor central
            user="rodrigo",        # Usuário do banco de dados central
            password="senha_segura",  # Senha do usuário
            database="central_monitoramento"  # Nome do banco de dados
        )
        print("Conexão com o banco de dados central bem-sucedida!")
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB central: {e}")
        return None

# Função para inserir log na tabela de logs
def inserir_log(raspberrypi_id, mensagem):
    conn_central = conectar_central()
    if conn_central:
        try:
            cursor_central = conn_central.cursor()

            # Verificar se o raspberrypi_id existe na tabela raspberrypis do banco central
            cursor_central.execute("SELECT id FROM raspberrypis WHERE id = ?", (raspberrypi_id,))
            result = cursor_central.fetchone()

            if result:  # Se encontrar, insere o log
                print(f"Inserindo log para o Raspberry Pi ID {raspberrypi_id}")
                cursor_central.execute("""
                    INSERT INTO logs (raspberrypi_id, mensagem)
                    VALUES (?, ?)
                """, (raspberrypi_id, mensagem))

                conn_central.commit()
                print(f"Log inserido com sucesso: {mensagem}")
            else:
                print(f"⚠️ Raspberry Pi com id {raspberrypi_id} não encontrado na tabela central.")

        except mariadb.Error as e:
            print(f"Erro ao inserir log: {e}")
        finally:
            conn_central.close()
    else:
        print("Erro ao conectar ao banco de dados central para inserir o log.")

# Exemplo de teste de inserção de log
inserir_log(1, "Mensagem de exemplo para o log.")
