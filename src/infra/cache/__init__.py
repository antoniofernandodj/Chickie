import abc
import redis
import json
import time
import pickle
from contextlib import suppress
from typing import Callable, TypeVar, Any, Union, Optional
with suppress(ModuleNotFoundError):
    from config import settings as s

T = TypeVar('T')


def get_function_key(function, *args, **kwargs):
    """
    Método para gerar uma chave para a funcao em questao com
    seus argumentos especificos
    """
    function_name: str
    if callable(function):
        function_name = str(function.__name__)
    else:
        function_name = str(function)

    data = {'function':function_name, 'args': args, 'kwargs': kwargs}
    dumps = str(data)
    return dumps


class CacheInterface(abc.ABC):

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

    @abc.abstractclassmethod
    def clear(self):
        pass


cache: CacheInterface


class RedisCache(CacheInterface):
    def __init__(self, host: str, port: int, db: int):
        self.redis_db = redis.Redis(host=host, port=port, db=db, password=s.REDIS_PASSWORD)
        self.redis_db.config_set('maxmemory-policy', 'allkeys-lru')
        self.__port = port
        self.__host = host
        self.get_function_key = get_function_key
        

    def __str__(self):
        return f'{type(self).__name__}(host={self.__host}, port={self.__port}, data={list(self.dict().keys())})'

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
        print('Armazenando dicionario ao redis')

        for key, value in data.items():
            self[key] = value

    def dict(self) -> dict:
        """
        Método para recuperar todos os pares chave-valor
        do cache como um dicionário.
        """
        print('Retornando dicionario do redis')

        keys = [key.decode() for key in self.redis_db.keys('*')]

        data = {}
        for key in keys:
            data[key] = self[key]

        return data
    
    def delete(self, key: str) -> None:
        print('Deletando chave do redis')
        self.redis_db.delete(key)

    def clear(self) -> None:
        print('Limpando cache do redis')
        keys = [key.decode() for key in self.redis_db.keys('*')]

        for key in keys:
            self.delete(key)


def get_cache() -> RedisCache:

    cache = RedisCache(
        host=s.REDIS_HOST,
        port=s.REDIS_PORT,
        db=s.REDIS_DB
    )
    cache['hello'] = 'world'
    # print('Redis inicializado')


    return cache


def cached_function(
        function: Callable[..., T],
        cache_time: Optional[int] = None,
        **kwargs
    ) -> T:

    cached: T
    cache = get_cache()
    start_time = time.perf_counter()
    
    key = cache.get_function_key(function=function, **kwargs)
    cached = cache[key]
    
    if cached is not None:
        # print("cached!")
        tf = f'{time.perf_counter() - start_time:.4f}'
        # print(f'Requisição {function.__name__} levou {tf} segundos')
        return cached

    result: T = function(**kwargs)
    # print("Not cached!")

    cache[key, cache_time] = result

    tf = f"{time.perf_counter() - start_time:.4f}"
    print(f"Requisição {function.__name__} levou {tf} segundos")
    return result