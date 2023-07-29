from src.infra.database.entities import Usuario
from src.infra.database.repositories import UsuarioRepository

user_data_1 = {
    'uuid': 'test-uuid-1',
    'name': 'Test User 1',
    'email': 'testuser@example.com',
    'password_hash': 'test_password_1',
}

user_data_2 = {
    'uuid': 'test-uuid-2',
    'name': 'Test User 2',
    'email': 'testuser2@example.com',
    'password_hash': 'test_password_2',
}

def test_create_user():

    # When
    user_uuid = UsuarioRepository.create(**user_data_1)
    user = UsuarioRepository.find_one(uuid=user_uuid)

    # Then
    assert user.uuid == user_data_1['uuid']
    assert user.name == user_data_1['name']
    assert user.email == user_data_1['email']
    assert user.password_hash != user_data_1['email']

def test_find_one_user():

    # When
    user = UsuarioRepository.find_one(uuid=user_data_1['uuid'])

    # Then
    assert user is not None
    assert user.uuid == user_data_1['uuid']

def test_find_all_users():
    # Given
    UsuarioRepository.create(**user_data_2)

    # When
    users = UsuarioRepository.find_all()

    # Then
    assert len(users) == 2

    assert users[0].uuid == user_data_1['uuid']
    assert users[0].name == user_data_1['name']
    assert users[0].email == user_data_1['email']
    assert users[0].password_hash != user_data_1['password_hash']

    assert users[1].uuid == user_data_2['uuid']
    assert users[1].name == user_data_2['name']
    assert users[1].email == user_data_2['email']
    assert users[1].password_hash != user_data_2['password_hash']

def test_remove_created_users():

    uuid1 = 'test-uuid-1'
    uuid2 = 'test-uuid-2'

    user1 = UsuarioRepository.find_one(uuid=uuid1)
    user2 = UsuarioRepository.find_one(uuid=uuid2)

    user1.delete()
    user2.delete()

    user1 = UsuarioRepository.find_one(uuid=uuid1)
    user2 = UsuarioRepository.find_one(uuid=uuid2)

    assert user1 is None
    assert user2 is None