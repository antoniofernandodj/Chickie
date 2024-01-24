from config import settings as s
from sqlalchemy.engine import create_engine


engine = create_engine(str(s.POSTGRES_URL))
engine_dev = create_engine(str(s.POSTGRES_URL_DEV))
engine_prod = create_engine(str(s.POSTGRES_URL_PROD))
