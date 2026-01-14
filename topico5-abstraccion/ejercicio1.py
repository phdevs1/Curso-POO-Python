from abc import ABC, abstractmethod
from typing import List, Optional


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}')"


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def list_all(self) -> List[User]:
        pass


class FileUserRepository(UserRepository):
    def __init__(self):
        self._users = []  # simulamos un archivo con una lista

    def save(self, user: User) -> None:
        self._users.append(user)

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None

    def list_all(self) -> List[User]:
        return self._users


class PostgresUserRepository(UserRepository):

    def save(self, user: User) -> None:
        print(f"[Postgres] INSERT INTO users VALUES ({user.user_id}, '{user.name}')")

    def get_by_id(self, user_id: int) -> Optional[User]:
        print(f"[Postgres] SELECT * FROM users WHERE id = {user_id}")
        return User(user_id, "UsuarioDesdePostgres")

    def list_all(self) -> List[User]:
        print("[Postgres] SELECT * FROM users")
        return [
            User(1, "Ana"),
            User(2, "Carlos")
        ]

# capa de negocio no depende de la implmentacion
# UserService solo conoce UserRepository, no sabe si es archivo o PostgreSQL.
# Principio SOLID (DIP): las capas de negocio no dependen de detalles
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_id: int, name: str):
        user = User(user_id, name)
        self.repository.save(user)

    def show_users(self):
        return self.repository.list_all()


file_repo = FileUserRepository()
service = UserService(file_repo)

service.create_user(1, "Pedro")
service.create_user(2, "Lucía")

print(service.show_users())

postgres_repo = PostgresUserRepository()
service = UserService(postgres_repo)

service.create_user(3, "María")
print(service.show_users())
