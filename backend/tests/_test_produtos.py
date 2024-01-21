from fastapi.testclient import TestClient
from faker import Faker
import pytest
import json
from random import randint
from dataclasses import dataclass
from typing import Optional


@dataclass
class Categoria:
    uuid: Optional[str]


categoria = Categoria(uuid=None)


f = Faker()

categoria_nome = f.word()
categoria_descricao = f.sentence()


produto = dict(
    nome=f.word(),
    descricao=f.sentence(),
    preco=randint(100, 999) / 100,
)

novo_produto = dict(
    nome=f.word(),
    descricao=f.sentence(),
    preco=randint(100, 999) / 100,
)


@pytest.fixture
def categoria_uuid(client: TestClient, access_token: str, loja_uuid: str):
    uuid = categoria.uuid
    if uuid is not None:
        return uuid

    payload = {
        "nome": categoria_nome,
        "descricao": categoria_descricao,
        "loja_uuid": loja_uuid,
    }
    response = client.post(
        "/categorias/",
        json=payload,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    categoria.uuid = str(json.loads(response.text)["uuid"])
    return categoria.uuid


def test_cadastrar_produto(
    client: TestClient, access_token: str, loja_uuid: str, categoria_uuid: str
):
    payload = {
        **produto,
        "categoria_uuid": categoria_uuid,
        "loja_uuid": loja_uuid,
    }
    response = client.post(
        "/produtos/",
        json=payload,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_requisitar_produtos(client: TestClient, loja_uuid: str):
    response = client.get("/produtos/", params={"loja_uuid": loja_uuid})
    assert response.status_code == 200


def test_requisitar_produto(client: TestClient, loja_uuid: str):
    response = client.get("/produtos/", params={"nome": produto["nome"]})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.get(f"/produtos/{valid_uuid}")
    assert response.status_code == 200
    # Add more assertions based on your expected response


def test_atualizar_produto_put_unauthorized(
    client: TestClient, loja_uuid: str, categoria_uuid: str
):
    response = client.get("/produtos/", params={"nome": produto["nome"]})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    payload = {
        **novo_produto,
        "uuid": valid_uuid,
        "loja_uuid": loja_uuid,
        "categoria_uuid": categoria_uuid,
    }
    response = client.put(f"/produtos/{valid_uuid}", json=payload)
    assert response.status_code == 401


def test_atualizar_produto_put(
    client: TestClient, loja_uuid: str, access_token: str, categoria_uuid: str
):
    response = client.get("/produtos/", params={"nome": produto["nome"]})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        **novo_produto,
        "uuid": valid_uuid,
        "loja_uuid": loja_uuid,
        "categoria_uuid": categoria_uuid,
    }
    response = client.put(
        f"/produtos/{valid_uuid}", json=payload, headers=headers
    )
    assert response.status_code == 200


def test_remover_produto_unouthorized(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/produtos/", params={"nome": novo_produto["nome"]})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(f"/produtos/{valid_uuid}")
    assert response.status_code == 401


def test_remover_produto(client: TestClient, access_token: str):
    response = client.get("/produtos/", params={"nome": novo_produto["nome"]})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(
        f"/produtos/{valid_uuid}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200
    assert json.loads(response.text)["itens_removed"] == 1


def test_unset_categoria(
    client: TestClient, access_token: str, categoria_uuid: str
):
    response = client.get(f"/categorias/{categoria_uuid}")
    valid_uuid = json.loads(response.text)["uuid"]
    response = client.delete(
        f"/categorias/{valid_uuid}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200
    assert json.loads(response.text)["itens_removed"] == 1
