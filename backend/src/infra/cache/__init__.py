import abc
import redis
import pickle
from contextlib import suppress
from typing import TypeVar, Any

with suppress(ModuleNotFoundError):
    from config import settings as s

T = TypeVar("T")


class Cache(abc.ABC):
    @abc.abstractmethod
    def __getitem__(self, key):
        pass

    @abc.abstractmethod
    def __setitem__(self, key: str, value: Any):
        pass

    @abc.abstractmethod
    def store_dict(self, data: dict):
        pass

    @abc.abstractmethod
    def dict(self):
        pass

    @abc.abstractmethod
    def delete(self, key: str):
        pass

    @abc.abstractmethod
    def clear(self):
        pass


class RedisCache(Cache):
    def __init__(self, host: str, port: int, db: int):
        self.redis_db = redis.Redis(
            host=host, port=port, db=db, password=s.REDIS_PASSWORD
        )
        self.redis_db.config_set("maxmemory-policy", "allkeys-lru")
        self.__port = port
        self.__host = host

    def __str__(self):
        return "{}(host={}, port={}, data={})".format(
            type(self).__name__,
            self.__host,
            self.__port,
            list(self.dict().keys()),
        )

    def __getitem__(self, key: str) -> Any:
        """Método para recuperar um valor do cache."""

        value = self.redis_db.get(key)
        if value:
            # print('Retornando cache do redis')
            return pickle.loads(value)

        return None

    def __setitem__(self, key: str, value: Any) -> None:
        """Método para definir um valor no cache."""

        # print('Atribuindo valor ao redis')

        # print('value to dump:', str(value))
        value_dumped = pickle.dumps(value)
        if isinstance(key, tuple):
            key_ttl = key[1]
            if key_ttl is None:
                key_ttl = s.CACHE_DEFAULT_TIMEOUT
            # print(f'Setting ttl as {key_ttl}')
            key_name = key[0]
            self.redis_db.setex(key_name, key_ttl, value_dumped)

        else:
            self.redis_db.setex(key, s.CACHE_DEFAULT_TIMEOUT, value_dumped)

    def store_dict(self, data: dict) -> None:
        """Método para armazenar um dicionário completo no cache."""
        print("Armazenando dicionario ao redis")

        for key, value in data.items():
            self[key] = value

    def dict(self) -> dict:
        """
        Método para recuperar todos os pares chave-valor
        do cache como um dicionário.
        """
        print("Retornando dicionario do redis")

        keys = [key.decode() for key in self.redis_db.keys("*")]

        data = {}
        for key in keys:
            data[key] = self[key]

        return data

    def delete(self, key: str) -> None:
        print("Deletando chave do redis")
        self.redis_db.delete(key)

    def clear(self) -> None:
        print("Limpando cache do redis")
        keys = [key.decode() for key in self.redis_db.keys("*")]

        for key in keys:
            self.delete(key)


def get_cache() -> RedisCache:
    cache = RedisCache(host=s.REDIS_HOST, port=s.REDIS_PORT, db=s.REDIS_DB)
    cache["hello"] = "world"

    return cache
