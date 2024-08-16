class Event:
    def __init__(self, name, address, category, time, description):
        # Inicializa um objeto Event com nome, endereço, categoria, horário e descrição
        self.name = name
        self.address = address
        self.category = category
        self.time = time
        self.description = description

    def to_dict(self):
        # Retorna uma representação em dicionário do objeto Event
        return {
            "name": self.name,
            "address": self.address,
            "category": self.category,
            "time": self.time,
            "description": self.description
        }

    def __str__(self):
        # Retorna uma representação em string do objeto Event
        return f"Event(name={self.name}, address={self.address}, category={self.category}, time={self.time}, description={self.description})"
