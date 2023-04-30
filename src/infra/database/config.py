from sqlalchemy.engine import create_engine
from config import settings as s
from src.infra.database.database_service import DatabaseService
from sqlalchemy.orm.session import sessionmaker
from time import sleep


database_url = "{0}+{1}://{2}:{3}@{4}/{5}".format(
    'postgresql', 'psycopg',
    s.POSTGRES_USERNAME, s.POSTGRES_PASSWORD,
    s.POSTGRES_HOST, s.POSTGRES_DATABASE
)

engine = create_engine(database_url)


def init_database():
    from src.infra.database.entities import Base
    
    DatabaseService.create_database(name=s.POSTGRES_DATABASE)
    Base.metadata.create_all(engine)
    

def get_db():
    while True:
        try:
            Session = sessionmaker(engine)
            return Session()
        except:
            sleep(5)
        
