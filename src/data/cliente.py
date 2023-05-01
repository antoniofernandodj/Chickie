from src.infra.database import entities as e
from src.infra.database import repository as r


def vincular(data: dict) -> dict:

    loja: e.Loja = r.Loja.find_one(uuid=data['loja_uuid'])
    usuario: e.Usuario = r.UsuarioRepository.find_one(uuid=data['usuario_uuid'])

    if loja is None or not isinstance(loja, e.Loja):
        response = {
            'message': f"Loja com UUID {loja.uuid} não encontrada.",
            'status': 'error',
            'status_code': 400,
            'redirect': None,
        }

        return response
    
    if usuario is None or not isinstance(usuario, e.Usuario):
        response = {
            'message': f"Usuário com UUID {usuario.uuid} não encontrado.",
            'status': 'error',
            'status_code': 400,
            'redirect': None,
        }

        return response
    
    if usuario in loja.usuarios:
        response = {
            'message': f"Usuário com UUID {usuario.uuid} já vinculado à loja.",
            'status': 'error',
            'status_code': 400,
            'redirect': None,
        }

        return response
    
    try:
        loja.vincular_comprador(usuario)

        response = {
            'message': 'Usuario vincuilado com sucesso.',
            'status': 'success',
            'status_code': 200,
            'redirect': None,
        }

        return response
    
    except Exception as error:

        response = {
            'message': str(error),
            'status': 'error',
            'status_code': 400,
            'redirect': None,
        }

        return response
