import psycopg2

class DatabaseManager:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password  
            )
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida!")
            return self.connection
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            raise Exception

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão encerrada.")

class CRUD(DatabaseManager):
    
    def create_table(self):
        try:
            sql_script = input("Insira o comando SQL para criar a tabela: ").upper()
            print(sql_script)
            with self.connection.cursor() as cursor:
                cursor.execute(sql_script)
            self.connection.commit() 
            print("Criação bem-sucedida!")
        except Exception as e:
            print(f"Criação falhou: {e}")
            self.connection.rollback()  

    def insert_data(self):
        try:   
            table = input("Insira o nome da tabela: ").upper() 
            columns = input("Insira as colunas e os valores (ex: col1, col2) VALUES (val1, val2): ")
            sql_query = f"INSERT INTO {table} {columns}"
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query)
            self.connection.commit()
            print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Inserção falhou: {e}")

    def read_data(self):
        try:
            table = input("Insira o nome da tabela: ").upper()
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table};")
                results = cursor.fetchall()
            print(results)
        except Exception as e:
            print(f"Consulta falhou: {e}")

   
    def delete_data(self):
        try:
            table = input("Insira o nome da tabela: ")
            with self.connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table};") 
            self.connection.commit()  
            print("Dados excluídos com sucesso!")
        except Exception as e:
            print(f"Incapaz de deletar: {e}")
            self.connection.rollback()  

    def commit(self):
        try:
            self.connection.commit()
            print("Mudanças confirmadas.")
        except Exception as e:
            print(f"Erro ao confirmar mudanças: {e}")
