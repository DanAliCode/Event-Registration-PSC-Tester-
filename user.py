class User:
    def __init__(self, username, password):
        # Inicializa um objeto User com nome de usuário e senha
        self.username = username
        self.password = password

    @staticmethod
    def verify_login(users, username, password):
        # Verifica se o nome de usuário e senha fornecidos correspondem a um usuário na lista
        for user in users:
            if user.username == username and user.password == password:
                return True
        return False

    def __str__(self):
        # Retorna uma representação em string do objeto User
        return f"{self.username}:{self.password}"
