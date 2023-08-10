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
        diaDaSemana = self.view.comboBoxProdutoPreco.currentText()[:3].lower()
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
        pass

    def cadastrarFornecedor(self):
        pass

    def cadastrarFuncionario(self):
        pass

    def cadastrarPedido(self):
        pass

    def cadastrarStatusPedido(self):
        pass

    def handleResponse(
        self, response: httpx.Response, successMessage: str = ""
    ) -> Optional[str]:
        if response.status_code == 200:
            return str(json.loads(response.text)[0]["uuid"])

        elif response.status_code == 201:
            self.showMessage("Success", successMessage)
            self.window.refreshUI()

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
