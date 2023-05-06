from src.infra.database.entities import Usuario


class LoginData:
    def __init__(self, user: Usuario, max_age: int):
        self.user = user
        self.max_age = max_age
