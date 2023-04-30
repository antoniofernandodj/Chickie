from config import settings as s
import psycopg

class DatabaseService:
    
    config = dict(
        user=s.POSTGRES_USERNAME,
        password=s.POSTGRES_PASSWORD,
        host=s.POSTGRES_HOST,
        port=s.POSTGRES_PORT
    )
    
    def __init__(self):
        self.__config = DatabaseService.config
        
        
    def __enter__(self) -> psycopg.cursor.Cursor:
        self.connector = psycopg.connect(**self.__config)
        self.cursor = self.connector.cursor()
        
        return self.cursor
    
    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type and exception_value and traceback:
            print({'exception_type': exception_type})
            print({'exception_value': exception_value})
            print(traceback)
            
        self.cursor.close()
    
    @classmethod
    def create_database(cls, name):
        connector = psycopg.connect(**cls.config)
        connector.autocommit = True
        cursor = connector.cursor()
        
        command = f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name}'"
        cursor.execute(command)
        
        exists = cursor.fetchone()
        if not exists:
            name = f"CREATE DATABASE {name}"
            cursor.execute(name)
        
        cursor.close()
        
    @classmethod
    def remove_database(cls, name):
        connector = psycopg.connect(**cls.config)
        connector.autocommit = True
        cursor = connector.cursor()
        
        command = f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name}'"
        cursor.execute(command)
        
        exists = cursor.fetchone()
        if exists:
            name = f"DROP DATABASE {name}"
            cursor.execute(name)
        
        cursor.close()