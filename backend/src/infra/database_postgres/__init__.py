"""
Este módulo é destinado a estabelecer uma conexão com um banco relacional
PostgreSQL, configurar sua classe de repositório e todas as dependencias
e modulos relacionados
"""

from config import settings

DSN = ("dbname={0} user={1} password={2} host={3}".format(
    settings.POSTGRES_DATABASE,
    settings.POSTGRES_USERNAME,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOST,
))

from . import config, session, entities  # noqa
