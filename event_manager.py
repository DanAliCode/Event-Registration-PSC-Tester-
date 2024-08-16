from datetime import datetime

class EventManager:
    def __init__(self):
        # Inicializa um gerenciador de eventos com uma lista vazia de eventos
        self.events = []

    def add_event(self, event):
        # Adiciona um evento à lista e ordena os eventos por data e hora
        self.events.append(event)
        self.sort_events()

    def list_events(self):
        # Lista todos os eventos com seus índices
        for i, event in enumerate(self.events, start=1):
            print(f"{i}. {event}")

    def confirm_participation(self, user, event):
        # Confirma a participação de um usuário em um evento
        print(f"{user.username} confirmou participação no evento {event.name}")

    def cancel_participation(self, user, event):
        # Cancela a participação de um usuário em um evento
        print(f"{user.username} cancelou participação no evento {event.name}")

    def set_events(self, events):
        # Define a lista de eventos e os ordena por data e hora
        self.events = events
        self.sort_events()

    def get_events(self):
        # Retorna a lista de eventos
        return self.events

    def sort_events(self):
        # Ordena os eventos por data e hora
        self.events.sort(key=lambda x: datetime.strptime(x.time, "%Y-%m-%d %H:%M"))
