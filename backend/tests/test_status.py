from fastapi.testclient import TestClient
from faker import Faker
import json

f = Faker()

status_nome = f.word()
status_descricao = f.sentence()

status_nome_2 = f.word()
status_descricao_2 = f.sentence()


def test_cadastrar_status_unauthorized(client: TestClient, loja_uuid: str):
    payload = {"nome": status_nome, "descricao": status_descricao}
    response = client.post("/status/", json=payload)
    assert response.status_code == 401


def test_cadastrar_status(
    client: TestClient, access_token: str, loja_uuid: str
):
    payload = {
        "nome": status_nome,
        "descricao": status_descricao,
        "loja_uuid": loja_uuid,
    }
    response = client.post(
        "/status/",
        json=payload,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_requisitar_status(client: TestClient, loja_uuid: str):
    response = client.get("/status/", params={"loja_uuid": loja_uuid})
    assert response.status_code == 200


def test_requisitar_many_status(client: TestClient, loja_uuid: str):
    response = client.get("/status/", params={"nome": status_nome})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.get(f"/status/{valid_uuid}")
    assert response.status_code == 200


def test_atualizar_status_put_unauthorized(
    client: TestClient, loja_uuid: str
):
    valid_uuid = "valid-uuid"
    payload = {
        "nome": status_nome_2,
        "descricao": status_descricao_2,
        "loja_uuid": loja_uuid,
    }
    response = client.put(f"/status/{valid_uuid}", json=payload)
    assert response.status_code == 401


def test_atualizar_status_put(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/status/", params={"nome": status_nome})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "uuid": valid_uuid,
        "nome": status_nome_2,
        "descricao": status_descricao_2,
        "loja_uuid": loja_uuid,
    }
    response = client.put(
        f"/status/{valid_uuid}", json=payload, headers=headers
    )
    assert response.status_code == 200


def test_remover_status_unouthorized(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/status/", params={"nome": status_nome_2})

    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(f"/status/{valid_uuid}")
    assert response.status_code == 401


def test_remover_status(
    client: TestClient, loja_uuid: str, access_token: str
):
    response = client.get("/status/", params={"nome": status_nome_2})
    valid_uuid = json.loads(response.text)[0]["uuid"]
    response = client.delete(
        f"/status/{valid_uuid}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    assert json.loads(response.text)["itens_removed"] == 1
