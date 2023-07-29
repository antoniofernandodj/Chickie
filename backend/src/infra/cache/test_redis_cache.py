
import pytest
import redis
from unittest.mock import MagicMock
import pickle
from config import settings
from . import RedisCache


@pytest.fixture
def redis_cache():
    # Configurar e retornar uma instância do RedisCache para cada teste
    host = 'localhost'
    port = 6379
    db = 0
    redis_cache = RedisCache(host, port, db)
    return redis_cache


def test_cache_init(redis_cache: RedisCache):
    # Testar a inicialização correta do objeto RedisCache
    assert isinstance(redis_cache.db, redis.Redis)
    assert redis_cache.db.connection_pool.connection_kwargs['host'] == 'localhost'
    assert redis_cache.db.connection_pool.connection_kwargs['port'] == 6379
    # assert redis_cache.db.db == 0


def test_cache_clear(redis_cache: RedisCache):
    redis_cache.clear()
    assert True


def test_cache_get_and_set(redis_cache: RedisCache):
    # Testar o método get do cache quando a chave existe
    key = 'my_key'
    value = 'my_value'
    redis_cache.set(key, value)
    assert redis_cache.get(key) == value


def test_cache_get_nonexistent(redis_cache: RedisCache):
    # Testar o método get do cache quando a chave não existe
    key = 'nonexistent_key'
    
    assert redis_cache.get(key) is None


def test_cache_setitem_and_getitem(redis_cache: RedisCache):
    # Testar o método setitem e get_item do cache
    key = 'my_key'
    value = 'my_value'
    
    redis_cache[key] = value
    assert redis_cache[key] == value


def test_cache_store_dict(redis_cache: RedisCache):
    # Testar o método store_dict do cache
    data = {'key1': 'value1', 'key2': 'value2'}
    
    redis_cache.store_dict(data)
    
    assert True


def test_cache_dict(redis_cache: RedisCache):
    # Testar o método dict do cache

    data = {'key1': 'value1', 'key2': 'value2', 'my_key': 'my_value'}
    stored = redis_cache.dict()
    
    assert stored == data


def test_cache_delete(redis_cache: RedisCache):
    # Testar o método delete do cache
    key = 'key1'
    
    redis_cache.delete(key)
    value = redis_cache.get(key)
    assert value is None


def test_cache_clear(redis_cache: RedisCache):
    # Testar o método clear do cache
    
    redis_cache.clear()
    assert {} == redis_cache.dict()
