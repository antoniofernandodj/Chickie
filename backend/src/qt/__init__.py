from . import views  # noqa
from src.infra.database.entities.endereco import UF
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.qt.controllers import Controller
import json
import httpx


class MainWindow(QMainWindow):
    def __init__(self, app):
        from src.qt.views.mainV2_ui import Ui_MainWindow

        super().__init__()

        self.app = app
        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.loja_uuid = "472d657d-7ed4-4431-bee9-dc0ccea98c73"

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsb2phIiwiZXhwIjoxNjkxNzE0MjUxfQ.Svc-Q6w6slwBuFYbD10NzzIaUVcvp9Y51bmi40tlEr4"  # noqa

        self.refreshUI()
        self.controller = Controller(
            view=self.view, app=self.app, window=self
        )
        self.controller.setup()

    def setupController(self):
        self.controller.setup()

    def refreshUI(self):
        self.view.comboBoxUFZonaEntrega.clear()
        self.view.comboBoxUFZonaEntrega.addItems([uf.name for uf in UF])

        self.view.comboBoxUFZonaEntrega.clear()
        self.view.comboBoxUFCliente.addItems([uf.name for uf in UF])

        response = httpx.get(
            "http://localhost:8000/categorias/",
            headers={"Authorization": f"Bearer {self.token}"},
        )

        if response.status_code == 200:
            categoriaList = json.loads(response.text)
            categoriaNomeList = [item["nome"] for item in categoriaList]

            self.view.comboBoxCategoriaProduto.clear()
            self.view.comboBoxCategoriaProduto.addItems(categoriaNomeList)

        elif response.status_code == 400:
            QMessageBox.critical(
                self.window, "Error", "Erro na requisição: dados inválidos."
            )
        elif response.status_code == 401:
            QMessageBox.critical(
                self.window, "Error", "Erro de sessão: Sua sessão expirou!"
            )
        elif response.status_code == 500:
            QMessageBox.critical(self.window, "Error", "Erro no servidor.")
        else:
            QMessageBox.critical(self.window, "Error", "Erro desconhecido.")

        self.controller = Controller(
            view=self.view, app=self.app, window=self
        )

        response = httpx.get(
            "http://localhost:8000/produtos/",
            headers={"Authorization": f"Bearer {self.token}"},
        )

        if response.status_code == 200:
            produtoList = json.loads(response.text)
            produtoNomeList = [item["nome"] for item in produtoList]

            self.view.comboBoxProdutoPreco.clear()
            self.view.comboBoxProdutoPreco.addItems(produtoNomeList)

        elif response.status_code == 400:
            QMessageBox.critical(
                self.window, "Error", "Erro na requisição: dados inválidos."
            )
        elif response.status_code == 401:
            QMessageBox.critical(
                self.window, "Error", "Erro de sessão: Sua sessão expirou!"
            )
        elif response.status_code == 500:
            QMessageBox.critical(self.window, "Error", "Erro no servidor.")
        else:
            QMessageBox.critical(self.window, "Error", "Erro desconhecido.")
