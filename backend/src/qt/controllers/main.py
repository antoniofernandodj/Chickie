import json
from contextlib import suppress
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMessageBox

from src.qt.controllers.base import BaseController

with suppress(ImportError):
    from src.qt.windows import MainWindow
    from src.qt.views.main_ui import Ui_MainWindow as MainView


class MainController(BaseController):
    categoriaCatastrada = Signal(str)
    produtoCatastrado = Signal(str)

    def __init__(self, view: "MainView", app, window: "MainWindow"):
        super().__init__()

        self.view = view
        self.app = app
        self.window = window

        self.categoriaCatastrada.connect(self.atualizarCategorias)
        self.produtoCatastrado.connect(self.atualizarProdutos)

        self.totalPedido = 0.0

    def setup(self):
        self.view.pushButtonCadastrarCategoriaProduto.clicked.connect(
            self.cadastrarCategoriaProduto
        )

        self.view.pushButtonCadastrarProduto.clicked.connect(
            self.cadastrarProduto
        )  # ####
        self.view.pushButtonCadastrarPreco.clicked.connect(
            self.cadastrarPreco
        )
        self.view.pushButtonCadastrarZonaEntrega.clicked.connect(
            self.cadastrarZonaEntrega
        )
        self.view.pushButtonCadastrarCliente.clicked.connect(
            self.cadastrarCliente
        )  # ####
        self.view.pushButtonCadastrarFornecedor.clicked.connect(
            self.cadastrarFornecedor
        )
        self.view.pushButtonCadastrarFuncionario.clicked.connect(
            self.cadastrarFuncionario
        )
        self.view.pushButtonCadastrarPedido.clicked.connect(
            self.cadastrarPedido
        )  # ####
        self.view.pushButtonCadastrarStatusPedido.clicked.connect(
            self.cadastrarStatusPedido
        )

        self.view.pushButtonAdicionarItemPedido.clicked.connect(
            self.adicionarItemNaLista
        )

        self.view.pushButtonRemoverItem.clicked.connect(
            self.removerItemDaLista
        )

        self.view.checkBoxFretePedido.clicked.connect(self.setFreteSpinBox)

    def setFreteSpinBox(self):
        if self.view.checkBoxFretePedido.isChecked():
            self.view.doubleSpinBoxFretePedido.hide()
        else:
            self.view.doubleSpinBoxFretePedido.show()

    def refreshtextBrowserTotalPedido(self):
        self.view.textBrowserTotalPedido.setText(f"R${self.totalPedido:.2f}")

    def adicionarItemNaLista(self):
        itemNome = self.view.comboBoxItemPedido.currentText()
        produto = self.window.produtos.getFromNome(itemNome)

        self.view.listWidgetItemPedido.addItem(
            f"{itemNome}\t(R${produto.preco})"
        )
        self.totalPedido += produto.preco
        self.refreshtextBrowserTotalPedido()

    def removerItemDaLista(self):
        selected_items = self.view.listWidgetItemPedido.selectedItems()
        for item in selected_items:
            itemNome = item.text()
            itemNome = itemNome.split("\t")[0]
            produto = self.window.produtos.getFromNome(itemNome)
            self.totalPedido -= produto.preco
            index = self.view.listWidgetItemPedido.row(item)
            self.view.listWidgetItemPedido.takeItem(index)
        self.refreshtextBrowserTotalPedido()

    def cadastrarCategoriaProduto(self):
        nome = self.view.lineEditNomeCategoriaProduto.text()
        descricao = (
            self.view.plainTextEditDescricaoCategoriaProduto.toPlainText()
        )  # ####

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
        self.categoriaCatastrada.emit(nome)

    def cadastrarProduto(self):
        nome = self.view.lineEditNomeProduto.text()
        produtoDescricao = self.view.textEditDescricaoProduto.toPlainText()
        categoriaNome = self.view.comboBoxCategoriaProduto.currentText()
        preco = self.view.doubleSpinBoxPrecoProduto.value()

        categoria = self.window.categorias.getFromNome(categoriaNome)
        if categoria is None:
            return

        categoria_uuid = categoria.uuid
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
        self.produtoCatastrado.emit(nome)

    def cadastrarPreco(self):
        produtoNome = self.view.comboBoxProdutoPreco.currentText()
        valor = self.view.doubleSpinValorPreco.value()
        diaDaSemana = self.view.comboBoxDiaDaSemanaPreco.currentText()[
            :3
        ].lower()  # ####

        produto = self.window.produtos.getFromNome(produtoNome)
        if produto is None:
            return

        produto_uuid = produto.uuid
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
            )  # ####
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
            )  # ####
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
        nome = self.view.lineEditNomeFornecedor
        username = self.view.lineEditUsernameFornecedor
        email = self.view.lineEditEmailFornecedor
        celular = self.view.lineEditCelularFornecedor
        telefone = self.view.lineEditTelefoneFornecedor
        CNPJ = self.view.lineEditCNPJFornecedor

        response = self.postRequest(
            "fornecedores/",
            json={
                "email": email,
                "username": username,
                "celular": celular,
                "telefone": telefone,
                "nome": nome,
                "CNPJ": CNPJ,
            },
        )

        try:
            self.handleResponse(
                response, "Fornecedor cadastrado com sucesso!"
            )
        except ValueError:
            return None

    def cadastrarFuncionario(self):
        nome = self.view.lineEditNomeFuncionario
        cargo = self.view.lineEditCargoFuncionario
        email = self.view.lineEditEmailFuncionario
        senha = self.view.lineEditSenhaFuncionario
        telefone = self.view.lineEditTelefoneFuncionario
        celular = self.view.lineEditCelularFuncionario

        response = self.postRequest(
            "fornecedores/",
            json={
                "email": email,
                "cargo": cargo,
                "senha": senha,
                "telefone": telefone,
                "nome": nome,
                "celular": celular,
            },
        )

        try:
            self.handleResponse(
                response, "Funcionario cadastrado com sucesso!"
            )  # ######
        except ValueError:
            return None

    def cadastrarPedido(self):
        status_uuid = self.view.comboBoxStatusPedido.currentText()
        frete = self.view.doubleSpinBoxFretePedido.value()
        loja_uuid = self.window.loja_uuid
        usuarioNome = self.view.comboBoxClientePedido.currentText()

        response = self.getRequest("usuarios/?nome={0}".format(usuarioNome))

        if response.status_code == 200:
            endereco_uuid = str(json.loads(response.text)[0]["endereco_uuid"])
        else:
            QMessageBox.critical(
                self.window,
                "Cadastro de Pedido",
                "Erro no cadastro do pedido",
            )

        usuario_uuid = self.handleResponse(response=response)
        if endereco_uuid is None or usuario_uuid is None:
            return None

        response = self.postRequest(
            "fornecedores/",
            json={
                "status_uuid": status_uuid,
                "frete": frete,
                "loja_uuid": loja_uuid,
                "usuario_uuid": usuario_uuid,
                "endereco_uuid": endereco_uuid,
            },
        )

        try:
            pedido_uuid = self.handleResponse(response=response)
        except ValueError:
            return None

        print(pedido_uuid)

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
            )  # ######
        except ValueError:
            return None

        self.view.lineEditNomeStatusPedido.clear()
        self.view.textEditDescricaoStatusPedido.clear()

    @Slot(str)
    def atualizarCategorias(self, categoriaNome: str):
        self.window.categorias.refresh()
        categoria = self.window.categorias.getFromNome(categoriaNome)
        if categoria is None:
            return
        self.view.comboBoxCategoriaProduto.addItem(categoria.nome)

    @Slot(str)
    def atualizarProdutos(self, produtoNome: str):
        self.window.produtos.refresh()
        produto = self.window.produtos.getFromNome(produtoNome)
        if produto is None:
            return

        self.view.comboBoxProdutoPreco.addItem(produto.nome)
        self.view.comboBoxItemPedido.addItem(produto.nome)
