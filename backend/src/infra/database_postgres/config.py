from time import sleep
from config import settings as s
from sqlalchemy.engine import create_engine
from src.infra.database_postgres.manager import DatabaseConnectionManager
from sqlalchemy.orm.session import sessionmaker


# database_url = "{0}+{1}://{2}:{3}@{4}/{5}".format(
#     "postgresql",
#     "psycopg2",
#     s.POSTGRES_USERNAME,
#     s.POSTGRES_PASSWORD,
#     s.POSTGRES_HOST,
#     s.POSTGRES_DATABASE,
# )

database_url = s.POSTGRES_URL

engine = create_engine(database_url)


async def init_database(database_name: str):
    from src.infra.database_postgres.entities import Base

    # await DatabaseConnectionManager.create_database(
    #     name=s.POSTGRES_DATABASE_PROD
    # )
    await DatabaseConnectionManager.create_database(name=database_name)
    Base.metadata.create_all(engine)


def get_session():
    session = None
    trying = True
    while trying:
        try:
            Session = sessionmaker(engine)
            session = Session()
            yield session
            trying = False
        except Exception:
            print('Waiting db...')
            sleep(5)

    if session:
        session.close()
