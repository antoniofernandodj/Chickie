from src.infra.database import entities as e
from src.infra.database import repository as r
from src.data.schema import VincularClienteDados, CadastrarLojaDados


def vincular_cliente(dados: VincularClienteDados) -> dict:

    loja: e.Loja = r.Loja.find_one(uuid=dados.loja_uuid)
    usuario: e.Usuario = r.UsuarioRepository.find_one(uuid=dados.usuario_uuid)

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

def cadastrar(dados: CadastrarLojaDados) -> dict:

    loja = r.LojaRepository.find_one(nome=dados.nome)

    if loja is not None:
        response = {
            'message': f'Loja com nome {dados["nome"]} já cadastrada!',
            'status': 'error'
        }

        return response
    
    if dados.password1 != dados.password2:
        response = {
            'message': f'Senhas diferentes.',
            'status': 'error'
        }

        return response

    loja = r.LojaRepository.create(
        nome = dados.nome,
        username = dados.username,
        email = dados.email,
        telefone = dados.telefone,
        celular = dados.celular,
        password_hash = dados.password2,
        grupo = dados.grupo
    )

    response = {
        'message': f'Loja criada com sucesso!',
        'status': 'error',
        'uuid': loja.uuid
    }

    return response
