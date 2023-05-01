from src.infra.database import entities as e
from src.infra.database import repository as r
from uuid import uuid4
from typing import Dict, List, Union


def cadastrar(data: Dict[str, Union[str, List[dict]]]) -> dict:

    precos_do_produto = r.Precos.find_all(produto_uuid=data['produto'])

    dias_da_semana_usados = [
        preco.dia_da_semana
        for preco in precos_do_produto
    ]

    messages = ''
    item_cadastrado = False

    for item in data['precos']:

        if item['dia_da_semana'] in dias_da_semana_usados:
            
            messages += f'Dia da semana {item["dia_da_semana"]} já em uso para este produto, por isso não cadastrado. '

        else:

            preco = e.Preco(
                uuid = uuid4(),
                produto_uuid = data['produto'],
                valor = item['valor'],
                dia_da_semana = item['dia_da_semana'],
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
        'status_code': 200,
        'redirect': None,
    }

    return response