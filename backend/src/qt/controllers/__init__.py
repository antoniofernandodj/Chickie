from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QObject
from contextlib import suppress
import json
import httpx
from typing import Optional

with suppress(ImportError):
    from src.qt.views.mainV2_ui import Ui_MainWindow
    from src.qt import MainWindow

# from src.qt.controllers.novo import ControllerNovo


class Controller(QObject):
    def __init__(self, view: "Ui_MainWindow", app, window: "MainWindow"):
        super().__init__()
        self.view = view
        self.app = app
        self.window = window

    def setup(self):
        self.view.pushButtonCadastrarCategoriaProduto.clicked.connect(
            self.cadastrarCategoriaProduto
        )

        self.view.pushButtonCadastrarProduto.clicked.connect(
            self.cadastrarProduto
        )
        self.view.pushButtonCadastrarPreco.clicked.connect(
            self.cadastrarPreco
        )
        self.view.pushButtonCadastrarZonaEntrega.clicked.connect(
            self.cadastrarZonaEntrega
        )
        self.view.pushButtonCadastrarCliente.clicked.connect(
            self.cadastrarCliente
        )
        self.view.pushButtonCadastrarFornecedor.clicked.connect(
            self.cadastrarFornecedor
        )
        self.view.pushButtonCadastrarFuncionario.clicked.connect(
            self.cadastrarFuncionario
        )
        self.view.pushButtonCadastrarPedido.clicked.connect(
            self.cadastrarPedido
        )
        self.view.pushButtonCadastrarStatusPedido.clicked.connect(
            self.cadastrarStatusPedido
        )

    def cadastrarCategoriaProduto(self):
        nome = self.view.lineEditNomeCategoriaProduto.text()
        descricao = (
            self.view.plainTextEditDescricaoCategoriaProduto.toPlainText()
        )

        response = self.postRequest(
            "categorias/",
            json={
                "nome": nome,
                "descricao": descricao,
                "loja_uuid": self.window.loja_uuid,
            },
        )
        try:
            self.handleResponse(
                response, "Categoria de produto cadastrado com sucesso!"
            )
        except ValueError:
            return None

        self.view.lineEditNomeCategoriaProduto.clear()
        self.view.plainTextEditDescricaoCategoriaProduto.clear()

    def cadastrarProduto(self):
        nome = self.view.lineEditNomeProduto.text()
        produtoDescricao = self.view.textEditDescricaoProduto.toPlainText()
        categoriaNome = self.view.comboBoxCategoriaProduto.currentText()
        preco = self.view.doubleSpinBoxPrecoProduto.value()

        response = self.getRequest(
            "categorias/?nome={0}".format(categoriaNome)
        )

        categoria_uuid = self.handleResponse(response=response)
        if categoria_uuid is None:
            return

        response = self.postRequest(
            "produtos/",
            json={
                "nome": nome,
                "descricao": produtoDescricao,
                "categoria_uuid": categoria_uuid,
                "loja_uuid": self.window.loja_uuid,
                "preco": preco,
            },
        )
        try:
            self.handleResponse(response, "Produto cadastrado com sucesso!")
        except ValueError:
            return None

        self.view.lineEditNomeProduto.clear()
        self.view.textEditDescricaoProduto.clear()
        self.view.doubleSpinBoxPrecoProduto.clear()

    def cadastrarPreco(self):
        produtoNome = self.view.comboBoxProdutoPreco.currentText()
        valor = self.view.doubleSpinValorPreco.value()
        diaDaSemana = self.view.comboBoxDiaDaSemanaPreco.currentText()[
            :3
        ].lower()

        response = self.getRequest("produtos/?nome={0}".format(produtoNome))
        produto_uuid = self.handleResponse(response=response)
        if produto_uuid is None:
            return

        response = self.postRequest(
            "precos/",
            json={
                "produto_uuid": produto_uuid,
                "valor": valor,
                "dia_da_semana": diaDaSemana,
            },
        )

        try:
            self.handleResponse(
                response, "Preço de produto cadastrado com sucesso!"
            )
        except ValueError:
            return None

        self.view.lineEditNomeZonaEntrega.clear()
        self.view.lineEditCidadeZonaEntrega.clear()
        self.view.lineEditBairroZonaEntrega.clear()
        self.view.lineEditCEPZonaEntrega.clear()

    def cadastrarZonaEntrega(self):
        nome = self.view.lineEditNomeZonaEntrega.text()
        cidade = self.view.lineEditCidadeZonaEntrega.text()
        Bairro = self.view.lineEditBairroZonaEntrega.text()
        CEP = self.view.lineEditCEPZonaEntrega.text()
        UF = self.view.comboBoxUFZonaEntrega.currentText()
        taxa = self.view.doubleSpinBoxTaxaZonaEntrega.value()

        response = self.postRequest(
            "zonas-de-entrega/",
            json={
                "nome": nome,
                "cidade": cidade,
                "uf": UF,
                "bairro": Bairro,
                "cep": CEP,
                "taxa_de_entrega": taxa,
                "loja_uuid": self.window.loja_uuid,
            },
        )

        try:
            self.handleResponse(
                response, "Zona de entrega cadastrada com sucesso!"
            )
        except ValueError:
            return None

        self.view.lineEditNomeZonaEntrega.clear()
        self.view.lineEditCidadeZonaEntrega.clear()
        self.view.lineEditBairroZonaEntrega.clear()
        self.view.lineEditCEPZonaEntrega.clear()

    def cadastrarCliente(self):
        nome = self.view.lineEditNomeCliente.text()
        email = self.view.lineEditEmailCliente.text()
        username = self.view.lineEditUsernameCliente.text()
        telefone = self.view.lineEditTelefoneCliente.text()
        celular = self.view.lineEditCelularCliente.text()
        senha = self.view.lineEditSenhaCliente.text()

        logradouro = self.view.lineEditLogradouroCliente.text()
        uf = self.view.comboBoxUFCliente.currentText()
        cidade = self.view.lineEditCidadeCliente.text()
        numero = self.view.lineEditNumeroCliente.text()
        bairro = self.view.lineEditBairroCliente.text()
        cep = self.view.lineEditCEPCliente.text()
        complemento = self.view.lineEditComplementoCliente.text()
        response = self.postRequest(
            "enderecos/",
            json={
                "uf": uf,
                "cidade": cidade,
                "logradouro": logradouro,
                "numero": numero,
                "nome": nome,
                "complemento": complemento,
                "bairro": bairro,
                "cep": cep,
            },
        )

        endereco_uuid = self.handleResponse(response=response)
        if endereco_uuid is None:
            return

        response = self.postRequest(
            "loja/cliente",
            json={
                "nome": nome,
                "username": username,
                "email": email,
                "telefone": telefone,
                "celular": celular,
                "endereco_uuid": endereco_uuid,
                "password": senha,
                "loja_uuid": self.window.loja_uuid,
            },
        )

        try:
            self.handleResponse(response, "Cliente cadastrado com sucesso!")
        except ValueError:
            return None

        self.view.lineEditNomeCliente.clear()
        self.view.lineEditEmailCliente.clear()
        self.view.lineEditUsernameCliente.clear()
        self.view.lineEditTelefoneCliente.clear()
        self.view.lineEditCelularCliente.clear()
        self.view.lineEditSenhaCliente.clear()

        self.view.lineEditLogradouroCliente.clear()
        self.view.lineEditCidadeCliente.clear()
        self.view.lineEditNumeroCliente.clear()
        self.view.lineEditBairroCliente.clear()
        self.view.lineEditCEPCliente.clear()
        self.view.lineEditComplementoCliente.clear()

    def cadastrarFornecedor(self):
        pass

    def cadastrarFuncionario(self):
        pass

    def cadastrarPedido(self):
        pass

    def cadastrarStatusPedido(self):
        nome = self.view.lineEditNomeStatusPedido.text()
        descricao = self.view.textEditDescricaoStatusPedido.toPlainText()

        response = self.postRequest(
            "status/",
            json={
                "nome": nome,
                "descricao": descricao,
                "loja_uuid": self.window.loja_uuid,
            },
        )

        try:
            self.handleResponse(
                response, "Status de pedido cadastrado com sucesso!"
            )
        except ValueError:
            return None

        self.view.lineEditNomeStatusPedido.clear()
        self.view.textEditDescricaoStatusPedido.clear()

    def handleResponse(
        self, response: httpx.Response, successMessage: str = ""
    ) -> Optional[str]:
        if response.status_code == 200:
            r = str(json.loads(response.text)[0]["uuid"])
            return r

        elif response.status_code == 201:
            if successMessage:
                self.showMessage("Success", successMessage)
            self.window.refreshUI()
            self.window.setupController()
            with suppress(Exception):
                r = str(json.loads(response.text)["uuid"])
                return r

        elif response.status_code == 400:
            self.showMessage("Error", "Erro na requisição: dados inválidos.")
            raise ValueError

        elif response.status_code == 401:
            self.showMessage("Error", "Erro de sessão: Sua sessão expirou!")
            raise ValueError

        elif response.status_code == 500:
            self.showMessage("Error", "Erro no servidor.")
            raise ValueError

        else:
            self.showMessage("Error", "Erro desconhecido.")
        return None

    def getRequest(self, endpoint: str):
        headers = {"Authorization": f"Bearer {self.window.token}"}
        response = httpx.get(
            f"http://localhost:8000/{endpoint}",
            headers=headers,
        )
        return response

    def postRequest(self, endpoint: str, json: dict) -> httpx.Response:
        headers = {"Authorization": f"Bearer {self.window.token}"}
        response = httpx.post(
            f"http://localhost:8000/{endpoint}", json=json, headers=headers
        )
        return response

    def showMessage(self, status: str, message: str) -> None:
        if status == "Success":
            QMessageBox.information(self.window, status, message)
        elif status == "Error":
            QMessageBox.critical(self.window, status, message)
