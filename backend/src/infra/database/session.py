from src.infra.database.config import engine
from sqlalchemy.orm.session import sessionmaker
from time import sleep


def get():
    while True:
        try:
            Session = sessionmaker(engine)
            return Session()
        except Exception:
            sleep(5)
