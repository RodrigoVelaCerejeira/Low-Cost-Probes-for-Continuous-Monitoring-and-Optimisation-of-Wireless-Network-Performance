import mariadb

def conectar_mysql():
    try:
        conn = mariadb.connect(
            host="localhost",
            user="monitor",
            password="senha_segura",
            database="monitoramento"
        )
        print("✅ Conexão com o MariaDB estabelecida com sucesso!")
        
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tabelas no banco:", tables)

        return conn
    
    except mariadb.Error as err:
        print(f"❌ Erro ao conectar ao MariaDB: {err}")
        return None

    finally:
        if 'conn' in locals():  # Verifica se a conexão foi criada antes de tentar fechar
            conn.close()
            print("🔌 Conexão encerrada.")

# Executar o teste de conexão
conectar_mysql()

