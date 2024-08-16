from user import User
from event import Event
from event_manager import EventManager
from data_handler import DataHandler

def main():
    event_manager = EventManager()
    data_handler = DataHandler()

    # Carregar usuários do arquivo
    users = data_handler.load_users("users.data")

    # Carregar eventos do arquivo
    events = data_handler.load_events("events.data")
    if events is None:
        print("Falha ao carregar eventos")
        return

    event_manager.set_events(events)

    user = None  # Definir a variável user fora do loop

    # Cadastro de usuário
    while True:
        print("Bem-vindo! Por favor, cadastre-se.")
        print("[1] Cadastrar usuario \n[2] Login \n[3] Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            # Cadastro de novo usuário
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            user = User(username, password)
            users.append(user)
            data_handler.save_users(users, "users.data")

        elif choice == '2':
            # Verificação de login
            print("Por favor, faça login.")
            login_username = input("Nome de usuário: ")
            login_password = input("Senha: ")

            if User.verify_login(users, login_username, login_password):
                print("Login bem-sucedido!")
                user = next(u for u in users if u.username == login_username)
                break
            else:
                print("Nome de usuário ou senha incorretos. Tente novamente.")

        elif choice == '3':
            print("Volte sempre!")
            return

    while True:
        print("\nMenu:")
        print("1. Cadastrar evento")
        print("2. Listar eventos")
        print("3. Confirmar participação em evento")
        print("4. Cancelar participação em evento")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Cadastro de evento
            event_name = input("Nome do evento: ")
            event_address = input("Endereço do evento: ")
            event_category = input("Categoria do evento: ")
            event_time = input("Horário do evento (YYYY-MM-DD HH:MM): ")
            event_description = input("Descrição do evento: ")
            event = Event(event_name, event_address, event_category, event_time, event_description)
            event_manager.add_event(event)
            data_handler.save_events(event_manager.get_events(), "events.data")
            print("Evento cadastrado com sucesso!")

        elif choice == "2":
            # Listar eventos
            event_manager.list_events()

        elif choice == "3":
            # Confirmar participação
            event_manager.list_events()
            event_index = int(input("Digite o número do evento para confirmar participação: ")) - 1
            if 0 <= event_index < len(event_manager.get_events()):
                event = event_manager.get_events()[event_index]
                event_manager.confirm_participation(user, event)
            else:
                print("Evento inválido.")

        elif choice == "4":
            # Cancelar participação
            event_manager.list_events()
            event_index = int(input("Digite o número do evento para cancelar participação: ")) - 1
            if 0 <= event_index < len(event_manager.get_events()):
                event = event_manager.get_events()[event_index]
                event_manager.cancel_participation(user, event)
                data_handler.save_events(event_manager.get_events(), "events.data")
                print("Participação cancelada com sucesso!")
            else:
                print("Evento inválido.")

        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
