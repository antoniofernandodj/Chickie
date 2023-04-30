from src.infra.database.entities.user import User
from src.infra import database
from werkzeug.security import generate_password_hash as gen_hash

def test_user_class():
    
    from faker import Faker
    
    fake = Faker()
    name = fake.name()
    email1 = fake.email()
    email2 = fake.email()
    word = fake.word()
    
    user = User(
        name=name,
        email=email1,
        password_hash=gen_hash(word)
    )
    
    user.save()

    with database.session.get() as session:
        query_user = session.query(User).filter_by(name=name).first()
        assert query_user is not None

    with database.session.get() as session:
        query_user = session.query(User).filter_by(name=name).first()
        query_user.update(email=email2)
        
        user_updated = session.query(User).filter_by(name=name, email=email2).first()
        assert user_updated is not None


    with database.session.get() as session:
        query_user = session.query(User).filter_by(name=name).first()
        query_user.delete()

    with database.session.get() as session:
        query_user = session.query(User).filter_by(name=name).first()
        assert query_user is None