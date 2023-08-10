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
        self.loja_uuid = "06da9970-efd8-4485-918a-0d4a3b3f0abd"

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsb2phIiwiZXhwIjoxNjkxNjQ0NzkyfQ.UhLHdzO_KFonSCzvHxx8RwxaokZYN9L0pzjxavBYs08"  # noqa

        self.refreshUI()
        self.controller = Controller(
            view=self.view, app=self.app, window=self
        )

    def refreshUI(self):
        self.view.comboBoxUFZonaEntrega.clear()
        self.view.comboBoxUFZonaEntrega.addItems([uf.value for uf in UF])

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
