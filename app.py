from experimento import CRUD

def execute(instance, option):
    available_options = {
        "1": instance.create_table,
        "2": instance.insert_data,
        "3": instance.read_data,
        "4": instance.delete_data,
        "5": instance.commit,
        "6": instance.close,
    }
    if option not in available_options:
        return
    available_options[option]()

def config_app():
    host = input("Insira o host do banco de dados: ")
    port = input("Insira a porta do banco de dados: ")
    database = input("Insira o nome do banco de dados: ")
    user = input("Insira o usuário do banco de dados: ")
    password = input("Insira a senha do banco de dados: ")

    db_manager = CRUD(host, port, database, user, password)

    try:
        db_manager.connect()
        return db_manager, True
    except Exception:
        print("As credenciais estão incorretas. Tente novamente.")
    
    return None, False

def serve_app(db_manager, connected):
    while connected:
        print("\nEscolha uma opção:")
        print("1: Criar tabela")
        print("2: Inserir dados")
        print("3: Ler dados")
        print("4: Deletar dados")
        print("5: Confirmar mudanças")
        print("6: Fechar conexão")
        print("0: Sair")

        option = input("Digite a opção desejada: ")

        if option not in [str(i) for i in range(7)]:
            print("Opção inválida! Tente novamente.")
            continue
        
        if option == '0':
            print("Saindo...")
            db_manager.close() 
            connected = False
        
        if option == '6':
            execute(db_manager, option)
            connected = False

        execute(db_manager, option)

def start_app():
    connected = False
    while not connected:
        db_manager, connected = config_app()
        if not connected:
            sair = input("Deseja finalizar a aplicação[s/n]")
            while sair not in ['s', 'n']:
                sair = input("Deseja finalizar a aplicação[s/n]")
            if sair == 's':
                break
    serve_app(db_manager, connected)
