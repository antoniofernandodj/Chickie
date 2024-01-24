"""
Este módulo é destinado a estabelecer uma conexão com um banco relacional
PostgreSQL, configurar sua classe de repositório e todas as dependencias
e modulos relacionados
"""

from config import settings
from typing import Optional

DSN = ("dbname={0} user={1} password={2} host={3}".format(
    settings.POSTGRES_DATABASE,
    settings.POSTGRES_USERNAME,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOST,
))


def get_dsn(mode: Optional[str] = None) -> str:
    match mode:
        case 'DEV':
            DSN = ("dbname={0} user={1} password={2} host={3}".format(
                settings.POSTGRES_DATABASE_DEV,
                settings.POSTGRES_USERNAME_DEV,
                settings.POSTGRES_PASSWORD_DEV,
                settings.POSTGRES_HOST_DEV,
            ))
        case 'PROD':
            DSN = ("dbname={0} user={1} password={2} host={3}".format(
                settings.POSTGRES_DATABASE_PROD,
                settings.POSTGRES_USERNAME_PROD,
                settings.POSTGRES_PASSWORD_PROD,
                settings.POSTGRES_HOST_PROD,
            ))
        case _:
            DSN = ("dbname={0} user={1} password={2} host={3}".format(
                settings.POSTGRES_DATABASE,
                settings.POSTGRES_USERNAME,
                settings.POSTGRES_PASSWORD,
                settings.POSTGRES_HOST,
            ))

    return DSN

from . import config, session, entities  # noqa
