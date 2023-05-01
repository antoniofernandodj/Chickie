from src.infra.database.entities.usuario import Usuario
from src.infra import database
from werkzeug.security import generate_password_hash as gen_hash

def test_usuario_class():
    
    from faker import Faker
    
    fake = Faker()
    name = fake.name()
    email1 = fake.email()
    email2 = fake.email()
    word = fake.word()
    
    usuario = Usuario(
        name=name,
        email=email1,
        password_hash=gen_hash(word)
    )
    
    usuario.save()

    with database.session.get() as session:
        query_usuario = session.query(Usuario).filter_by(name=name).first()
        assert query_usuario is not None

    with database.session.get() as session:
        query_usuario = session.query(Usuario).filter_by(name=name).first()
        query_usuario.update(email=email2)
        
        usuario_updated = session.query(Usuario).filter_by(name=name, email=email2).first()
        assert usuario_updated is not None


    with database.session.get() as session:
        query_usuario = session.query(Usuario).filter_by(name=name).first()
        query_usuario.delete()

    with database.session.get() as session:
        query_usuario = session.query(Usuario).filter_by(name=name).first()
        assert query_usuario is None