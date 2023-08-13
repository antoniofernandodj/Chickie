from fastapi.testclient import TestClient
from faker import Faker
import json

f = Faker()
categoria_nome = f.word()
categoria_descricao = f.sentence()

categoria_nome_2 = f.word()
categoria_descricao_2 = f.sentence()


def test_cadastrar_categorias_unauthorized(
    client: TestClient, loja_uuid: str
):
    payload = {"nome": categoria_nome, "descricao": categoria_descricao}
    response = client.post("/categorias/", json=payload)
    assert response.status_code == 401


def test_cadastrar_categorias(
    client: TestClient, access_token: str, loja_uuid: str
):
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
    assert response.status_code == 201


def test_requisitar_categorias(client: TestClient, loja_uuid: str):
    response = client.get("/categorias/", params={"loja_uuid": loja_uuid})
    assert response.status_code == 200


def test_requisitar_categoria(client: TestClient, loja_uuid: str):
    response = client.get("/categorias/", params={"nome": categoria_nome})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.get(f"/categorias/{valid_uuid}")
    assert response.status_code == 200
    # Add more assertions based on your expected response


# def test_atualizar_categoria_patch(client: TestClient):
#     # Assuming you have a valid UUID for testing
#     valid_uuid = "valid-uuid"
#     response = client.patch(f"/categorias/{valid_uuid}")
#     assert response.status_code == 200


def test_atualizar_categoria_put_unauthorized(
    client: TestClient, loja_uuid: str
):
    valid_uuid = "valid-uuid"
    payload = {
        "nome": categoria_nome_2,
        "descricao": categoria_descricao_2,
        "loja_uuid": loja_uuid,
    }
    response = client.put(f"/categorias/{valid_uuid}", json=payload)
    assert response.status_code == 401


def test_atualizar_categoria_put(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/categorias/", params={"nome": categoria_nome})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "uuid": valid_uuid,
        "nome": categoria_nome_2,
        "descricao": categoria_descricao_2,
        "loja_uuid": loja_uuid,
    }
    response = client.put(
        f"/categorias/{valid_uuid}", json=payload, headers=headers
    )
    assert response.status_code == 200


def test_remover_categoria_unouthorized(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/categorias/", params={"nome": categoria_nome_2})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(f"/categorias/{valid_uuid}")
    assert response.status_code == 401


def test_remover_categoria(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/categorias/", params={"nome": categoria_nome_2})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(
        f"/categorias/{valid_uuid}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    assert json.loads(response.text)["itens_removed"] == 1
