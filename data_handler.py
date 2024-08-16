import json
from user import User
from event import Event

class DataHandler:
    def load_events(self, file_path):
        # Carrega eventos de um arquivo JSON
        try:
            with open(file_path, "r") as file:
                load = file.read().strip()
                if not load:
                    print("O arquivo de eventos está vazio.")
                    return []
                events_data = json.loads(load)
                events = [Event(**event) for event in events_data]
                return events
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Erro ao carregar eventos: {e}")
            return []

    def save_events(self, events, filename):
        # Salva eventos em um arquivo JSON
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump([event.to_dict() for event in events], file)
        except IOError as e:
            print(f"Erro ao salvar eventos: {e}")

    def load_users(self, file_path):
        # Carrega usuários de um arquivo de texto
        try:
            with open(file_path, "r") as file:
                users = []
                for line in file:
                    if ":" in line:
                        username, password = line.strip().split(":")
                        users.append(User(username, password))
                    else:
                        print(f"Linha inválida no arquivo de usuários: {line.strip()}")
                return users
        except (FileNotFoundError, IOError) as e:
            print(f"Erro ao carregar usuários: {e}")
            return []

    def save_users(self, users, filename):
        # Salva usuários em um arquivo de texto
        try:
            with open(filename, "w") as file:
                for user in users:
                    file.write(str(user) + "\n")
        except IOError as e:
            print(f"Erro ao salvar usuários: {e}")
