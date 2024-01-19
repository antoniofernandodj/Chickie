from time import sleep
from config import settings as s
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


database_url = s.POSTGRES_URL

engine = create_engine(database_url)


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
