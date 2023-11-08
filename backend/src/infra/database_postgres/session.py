from src.infra.database_postgres.config import engine
from sqlalchemy.orm.session import sessionmaker
from time import sleep


def get():
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
