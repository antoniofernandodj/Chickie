from src.infra.database import entities as e
from src.infra.database import repository as r


def vincular_cliente(data: dict) -> dict:

    loja: e.Loja = r.Loja.find_one(uuid=data['loja_uuid'])
    usuario: e.Usuario = r.UsuarioRepository.find_one(uuid=data['usuario_uuid'])

    if loja is None or not isinstance(loja, e.Loja):
        response = {
            'message': f"Loja com UUID {loja.uuid} não encontrada.",
            'status': 'error'
        }

        return response
    
    if usuario is None or not isinstance(usuario, e.Usuario):
        response = {
            'message': f"Usuário com UUID {usuario.uuid} não encontrado.",
            'status': 'error'
        }

        return response
    
    if usuario in loja.usuarios:
        response = {
            'message': f"Usuário com UUID {usuario.uuid} já vinculado à loja.",
            'status': 'error'
        }

        return response
    
    try:
        loja.vincular_comprador(usuario)

        response = {
            'message': 'Usuario vinculado com sucesso.',
            'status': 'success'
        }

        return response
    
    except Exception as error:

        response = {
            'message': str(error),
            'status': 'error'
        }

        return response

def cadastrar(data: dict) -> dict:
    loja = r.LojaRepository.find_one(nome=data['nome'])

    if loja is not None:
        response = {
            'message': f'Loja com nome {data["nome"]} já cadastrada!',
            'status': 'error'
        }

        return response
    
    r.LojaRepository.create(
        nome = '',
        username = '',
        email = '',
        telefone = '',
        celular = '',
        password_hash = '',
        grupo = ''
    )
    
    loja = e.Loja(

    )

