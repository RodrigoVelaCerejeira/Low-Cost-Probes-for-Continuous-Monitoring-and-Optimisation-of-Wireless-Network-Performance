import mariadb

def conectar_central():
    try:
        conn = mariadb.connect(
            host="IP_DO_SERVIDOR_CENTRAL",
            user="monitor",
            password="senha_segura",
            database="central_monitoramento"
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao MariaDB central: {e}")
        return None

def inserir_log(raspberrypi_id, mensagem):
    conn_central = conectar_central()
    if conn_central:
        try:
            cursor_central = conn_central.cursor()

            cursor_central.execute("""
                INSERT INTO logs (raspberrypi_id, mensagem)
                VALUES (?, ?)
            """, (raspberrypi_id, mensagem))

            conn_central.commit()
            print("Log inserido com sucesso!")

        except mariadb.Error as e:
            print(f"Erro ao inserir log: {e}")
        finally:
            conn_central.close()
    else:
        print("Erro ao conectar ao banco de dados central para inserir o log.")
