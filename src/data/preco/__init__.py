from src.infra.database import entities as e
from src.infra.database import repository as r
from uuid import uuid4
from src.data.schema import PrecoDados


def cadastrar(dados: PrecoDados) -> dict:

    precos_do_produto = r.PrecosRepository.find_all(
        produto_uuid=dados.produto_uuid
    )

    dias_da_semana_usados = [
        preco.dia_da_semana
        for preco in precos_do_produto
    ]

    messages = ''
    item_cadastrado = False

    for dado in dados.precos:

        if dado.dia_da_semana in dias_da_semana_usados:
            messages += f'Dia da semana {dado.dia_da_semana} já em uso para este produto, por isso não cadastrado. '

        else:
            preco = e.Preco(
                uuid = uuid4(),
                produto_uuid = dados.produto_uuid,
                valor = dado.valor,
                dia_da_semana = dado.dia_da_semana,
            )

            preco.save()
            item_cadastrado = True

    if item_cadastrado:
        message = 'Preços cadastrados com sucesso! Aviso: ' + messages
        status = 'warning'

    else:
        message = 'Preços cadastrados com sucesso!'
        status = 'success'

    response = {
        'message': message,
        'status': status,
    }

    return response
