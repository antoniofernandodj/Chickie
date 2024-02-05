import json
from contextlib import suppress
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import (
    QMessageBox,
    QTableWidgetItem,
    QTableWidget,
)


from domain.services import AuthService, ProdutoService, CategoriaService
from domain.models import ItemPedidoPOST
from services import FileService
from typing import Optional
from models import PrecosModel, ProdutosModel, IngredienteModel
from __feature__ import snake_case, true_property  # type: ignore  # noqa
import os

from domain.models import (  # noqa
    Produto,
    ProdutoPOST,
    CategoriaProdutos,
    Funcionario,
    ZonaDeEntrega,
    Pedido,
    ItemPedido
)

from controllers.base import BaseController

with suppress(ImportError):
    from windows import MainWindow
    from views.main_ui import Ui_MainWindow as MainView


class MainController(BaseController):
    categoria_catastrada = Signal(CategoriaProdutos)
    produto_catastrado = Signal(str)

    def __init__(self, view: "MainView", app, window: "MainWindow"):
        super().__init__()

        self.view = view
        self.app = app
        self.window = window

        self.auth_service = AuthService()
        self.categoria_service = CategoriaService()
        self.produto_service = ProdutoService()

        self.produto_model = ProdutosModel(self.window)
        self.preco_model = PrecosModel(self.window)
        self.ingrediente_model = IngredienteModel(self.window)

        self.total_pedido = 0.0

    def setup(self):
        self.loja = self.auth_service.get_loja_data()

        self.view.table_widget_item_pedido.row_count = 0

        # Let's register callbacks!!!
        cb = self.remover_item_na_lista
        self.view.table_widget_item_pedido.itemDoubleClicked.connect(cb)

        cb = self.update_precos
        self.view.combo_box_produto_preco.currentIndexChanged.connect(cb)

        cb = self.cadastrar_categoria_produto
        self.view.push_button_cadastrar_categoria_produto.clicked.connect(cb)

        cb = self.cadastrar_produto
        self.view.push_button_cadastrar_produto.clicked.connect(cb)

        cb = self.cadastrar_preco
        self.view.push_button_cadastrar_preco.clicked.connect(cb)

        cb = self.cadastrar_cliente
        self.view.push_button_cadastrar_cliente.clicked.connect(cb)

        cb = self.cadastrar_pedido
        self.view.push_button_cadastrar_pedido.clicked.connect(cb)

        cb = self.cadastrar_status_pedido
        self.view.push_button_cadastrar_status_pedido.clicked.connect(cb)

        cb = self.adicionar_item_na_lista
        self.view.push_button_adicionar_item_pedido.clicked.connect(cb)

        cb = self.atualizar_categorias
        self.categoria_catastrada.connect(cb)

        cb = self.atualizar_produtos
        self.produto_catastrado.connect(cb)

        cb = self.set_frete_spin_box
        self.view.check_box_frete_pedido.clicked.connect(cb)

        # self.view.pushButtonCadastrarFornecedor.clicked.connect(
        #     self.cadastrar_fornecedor
        # )
        # self.view.pushButtonCadastrarFuncionario.clicked.connect(
        #     self.cadastrar_funcionario
        # )
        # self.view.pushButtonCadastrarZonaEntrega.clicked.connect(
        #     self.cadastrar_zona_entrega
        # )

    def set_frete_spin_box(self):
        if self.view.check_box_frete_pedido.checked:  # type: ignore
            self.view.double_spin_box_frete_pedido.hide()
        else:
            self.view.double_spin_box_frete_pedido.show()

    def refresh_text_browser_total_pedido(self):
        fmt = f"R${self.total_pedido:.2f}"
        self.view.line_edit_total_item_pedido.text = fmt

    def get_table_row_items(self, table_widget: QTableWidget):
        items_in_row: list[str] = []

        selected_row = table_widget.current_row()
        for col in range(table_widget.column_count):
            item = table_widget.item(selected_row, col)
            if item:
                items_in_row.append(item.text())

        return items_in_row

    def remover_item_na_lista(self, item: QTableWidgetItem) -> None:
        table_widget = self.view.table_widget_item_pedido

        selected_row = table_widget.current_row()

        items_in_row = self.get_table_row_items(table_widget)

        preco = float(items_in_row[1])
        quantidade = int(items_in_row[2])
        subtotal = preco * quantidade

        if selected_row >= 0:
            table_widget.remove_row(selected_row)

        self.total_pedido -= subtotal
        self.refresh_text_browser_total_pedido()

    def adicionar_item_na_lista(self) -> None:
        combo_box = self.view.combo_box_item_pedido
        produto: Optional[Produto] = combo_box.current_data()
        if produto is None or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.critical(self.window, title, message)
            return

        quantidade = self.view.spin_box_item_pedido.value
        subtotal = produto.preco * quantidade

        ip = ItemPedidoPOST(
            quantidade=self.view.spin_box_item_pedido.value,
            observacoes=self.view.text_edit_observacao_item.plain_text,
            produto_uuid=produto.uuid,
            ingredientes=[],
            loja_uuid=self.loja.uuid
        )

        ingredientes_nomes: list[str] = []

        for ingrediente_sel in ip.ingredientes:
            if ingrediente_sel.value is True:
                ingrediente = self.ingrediente_model.get(ingrediente_sel.uuid)
                ingredientes_nomes.append(ingrediente.nome or '')

        table_widget = self.view.table_widget_item_pedido

        r = table_widget.row_count
        table_widget.insert_row(r)

        row = [
            QTableWidgetItem(produto.nome),
            QTableWidgetItem(str(produto.preco)),
            QTableWidgetItem(str(ip.quantidade)),
            QTableWidgetItem(str(produto.preco * ip.quantidade)),
            QTableWidgetItem(ip.observacoes),
            QTableWidgetItem(', '.join(ingredientes_nomes))
        ]

        for col, item in enumerate(row):
            # QTableWidgetItem
            item.set_flags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            table_widget.set_item(r, col, item)

        self.total_pedido += subtotal
        self.refresh_text_browser_total_pedido()

        self.view.text_edit_observacao_item.clear()
        self.view.spin_box_item_pedido.value = 1  # type: ignore
        self.view.spin_box_quantidade_acicionais.value = 0   # type: ignore

    def cadastrar_categoria_produto(self):
        text_edit = self.view.plain_text_edit_descricao_categoria_produto

        nome = self.view.line_edit_nome_categoria_produto.text
        descricao = text_edit.plain_text

        categoria = CategoriaProdutos(
            nome=nome,
            descricao=descricao,
            loja_uuid=self.loja.uuid
        )

        response = self.categoria_service.save(categoria)
        categoria.uuid = response.json()['uuid']

        try:
            success_msg = "Categoria de produto cadastrado com sucesso!"
            self.handle_response(response, success_msg)
        except ValueError:
            return None

        self.view.line_edit_nome_categoria_produto.clear()
        self.view.plain_text_edit_descricao_categoria_produto.clear()
        self.categoria_catastrada.emit(categoria)

    def cadastrar_produto(self) -> None:
        label = self.view.label_produto_image_filename
        nome = self.view.line_edit_nome_produto.text
        produto_descricao = self.view.text_edit_descricao_produto.plain_text

        categoria: CategoriaProdutos = (
            self.view.combo_box_categoria_produto.current_data()
        )
        if (
            categoria is None or
            categoria.uuid is None or
            not isinstance(categoria.uuid, str)
        ):
            title = 'Aviso'
            message = 'Escolha ao menos uma categoria!'
            QMessageBox.critical(self.window, title, message)
            return

        preco = self.view.double_spin_box_preco_produto.value

        produto = ProdutoPOST(
            nome=nome,
            descricao=produto_descricao,
            categoria_uuid=categoria.uuid,
            loja_uuid=self.loja.uuid,
            preco=preco,
            image_bytes=FileService.get_base64_string(label=label),
            filename=os.path.basename(label.text)
        )

        response = self.produto_service.save(produto)

        try:
            self.handle_response(response, "Produto cadastrado com sucesso!")
        except ValueError:
            return None

        self.view.line_edit_nome_produto.clear()
        self.view.text_edit_descricao_produto.clear()
        self.view.double_spin_box_preco_produto.clear()
        self.produto_catastrado.emit(produto)
        label.clear()

    def cadastrar_preco(self):
        produto = self.view.combo_box_produto_preco.current_data()

        valor = self.view.double_spin_valor_preco.value
        combo = self.view.combo_box_dia_da_semana_preco
        dia_da_semana = combo.current_text[:3].lower()

        if produto is None or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.critical(self.window, title, message)
            return

        body = {
            "produto_uuid": produto.uuid,
            "valor": valor,
            "dia_da_semana": dia_da_semana,
        }

        response = self.post_request("precos/", json=body)

        try:
            msg = "Preço de produto cadastrado com sucesso!"
            self.handle_response(response, msg)  # ####
        except ValueError:
            return None

        # self.view.lineEditNomeZonaEntrega.clear()
        # self.view.lineEditCidadeZonaEntrega.clear()
        # self.view.lineEditBairroZonaEntrega.clear()
        # self.view.lineEditCEPZonaEntrega.clear()

    def cadastrar_cliente(self):
        nome = self.view.line_edit_nome_cliente.text
        email = self.view.line_edit_email_cliente.text
        username = self.view.line_edit_username_cliente.text
        telefone = self.view.line_edit_telefone_cliente.text
        celular = self.view.line_edit_celular_cliente.text
        senha = '123456'

        logradouro = self.view.line_edit_logradouro_cliente.text
        uf = self.view.combo_box_uf_cliente.current_text
        cidade = self.view.line_edit_cidade_cliente.text
        numero = self.view.line_edit_numero_cliente.text
        bairro = self.view.line_edit_bairro_cliente.text
        cep = self.view.line_edit_cep_cliente.text
        complemento = self.view.line_edit_complemento_cliente.text

        body = {
            "uf": uf,
            "cidade": cidade,
            "logradouro": logradouro,
            "numero": numero,
            "nome": nome,
            "complemento": complemento,
            "bairro": bairro,
            "cep": cep,
        }

        response = self.post_request("enderecos/", json=body)

        endereco_uuid = self.handle_response(response=response)
        if endereco_uuid is None:
            title = 'Aviso'
            message = 'Erro no cadastro do endereço!'
            QMessageBox.critical(self.window, title, message)
            return

        body = {
            "nome": nome,
            "username": username,
            "email": email,
            "telefone": telefone,
            "celular": celular,
            "endereco_uuid": endereco_uuid,
            "password": senha,
            "loja_uuid": self.loja.uuid,
        }

        response = self.post_request("loja/cliente", json=body)

        try:
            self.handle_response(response, "Cliente cadastrado com sucesso!")
        except ValueError:
            return None

        self.view.line_edit_nome_cliente.clear()
        self.view.line_edit_email_cliente.clear()
        self.view.line_edit_username_cliente.clear()
        self.view.line_edit_telefone_cliente.clear()
        self.view.line_edit_celular_cliente.clear()

        self.view.line_edit_logradouro_cliente.clear()
        self.view.line_edit_cidade_cliente.clear()
        self.view.line_edit_numero_cliente.clear()
        self.view.line_edit_bairro_cliente.clear()
        self.view.line_edit_cep_cliente.clear()
        self.view.line_edit_complemento_cliente.clear()

    def cadastrar_pedido(self):
        frete = self.view.double_spin_box_frete_pedido.value
        loja_uuid = self.loja.uuid
        usuario_nome = self.view.combo_box_cliente_pedido.current_text

        response = self.get_request("usuarios/?nome={0}".format(usuario_nome))

        if response.status_code == 200:
            endereco_uuid = str(json.loads(response.text)[0]["endereco_uuid"])
        else:
            title = "Cadastro de Pedido"
            text = "Erro no cadastro do pedido"
            QMessageBox.critical(self.window, title, text)
            return

        usuario_uuid = self.handle_response(response=response)
        if endereco_uuid is None or usuario_uuid is None:
            title = 'Aviso'
            message = 'Erro no cadastro!'
            QMessageBox.critical(self.window, title, message)
            return

        body = {
            "status_uuid": None,
            "frete": frete,
            "loja_uuid": loja_uuid,
            "usuario_uuid": usuario_uuid,
            "endereco_uuid": endereco_uuid,
        }

        response = self.post_request("fornecedores/", json=body)

        try:
            pedido_uuid = self.handle_response(response=response)
        except ValueError:
            return None

        print(pedido_uuid)

    def cadastrar_status_pedido(self):
        nome = self.view.line_edit_nome_status_pedido.text
        descricao = self.view.text_edit_descricao_status_pedido.plain_text

        body = {
            "nome": nome,
            "descricao": descricao,
            "loja_uuid": self.loja.uuid,
        }

        response = self.post_request(endpoint="status/", json=body)

        try:
            msg = "Status de pedido cadastrado com sucesso!"
            self.handle_response(response, msg)
        except ValueError:
            return None

        self.view.line_edit_nome_status_pedido.clear()
        self.view.text_edit_descricao_status_pedido.clear()

    @Slot(CategoriaProdutos)
    def atualizar_categorias(self, categoria: CategoriaProdutos):
        self.window.categorias.refresh()
        id = categoria.uuid
        if id is None:
            raise

        nome = categoria.nome
        self.view.combo_box_categoria_produto.add_item(nome, userData=id)

    @Slot(Produto)
    def atualizar_produtos(self, produto: Produto):
        p = produto
        self.window.produtos.refresh()
        self.view.combo_box_produto_preco.add_item(produto.nome, userData=p)
        self.view.combo_box_item_pedido.add_item(produto.nome, userData=p)

    @Slot(Produto)
    def atualizar_ingredientes(self, produto: Produto):
        if produto.uuid is None:
            raise

        ingredientes = self.ingrediente_model.get_data(produto.uuid)
        for ingrediente in ingredientes:
            print({'ingrediente': ingrediente})

    def update_precos(self) -> None:
        combo_box = self.view.combo_box_produto_preco
        produto: Optional[Produto] = combo_box.current_data()
        if produto is None or produto.uuid is None:
            return

        table_widget = self.view.table_widget_precos_cadastrados
        table_widget.row_count = 0
        for preco in self.preco_model.get_data(produto_uuid=produto.uuid):

            table_widget.insert_row(0)

            row = [
                QTableWidgetItem(preco.dia_da_semana),
                QTableWidgetItem(str(preco.valor))
            ]

            for col, item in enumerate(row):
                table_widget.set_item(0, col, item)


"""
    def cadastrar_fornecedor(self):
        nome = self.view.lineEditNomeFornecedor
        username = self.view.lineEditUsernameFornecedor
        email = self.view.lineEditEmailFornecedor
        celular = self.view.lineEditCelularFornecedor
        telefone = self.view.lineEditTelefoneFornecedor
        CNPJ = self.view.lineEditCNPJFornecedor

        body = {
            "email": email,
            "username": username,
            "celular": celular,
            "telefone": telefone,
            "nome": nome,
            "CNPJ": CNPJ,
        }

        response = self.post_request("fornecedores/", json=body)

        try:
            self.handle_response(
                response, "Fornecedor cadastrado com sucesso!"
            )
        except ValueError:
            return None

    def cadastrar_funcionario(self):
        nome = self.view.lineEditNomeFuncionario
        cargo = self.view.lineEditCargoFuncionario
        email = self.view.lineEditEmailFuncionario
        senha = self.view.lineEditSenhaFuncionario
        telefone = self.view.lineEditTelefoneFuncionario
        celular = self.view.lineEditCelularFuncionario

        body = {
            "email": email,
            "cargo": cargo,
            "senha": senha,
            "telefone": telefone,
            "nome": nome,
            "celular": celular,
        }

        response = self.post_request("fornecedores/", json=body)

        try:
            msg = "Funcionario cadastrado com sucesso!"
            self.handle_response(response, msg)  # ######
        except ValueError:
            return None

    def cadastrar_zona_entrega(self):
        nome = self.view.lineEditNomeZonaEntrega.text
        cidade = self.view.lineEditCidadeZonaEntrega.text
        Bairro = self.view.lineEditBairroZonaEntrega.text
        CEP = self.view.lineEditCEPZonaEntrega.text
        UF = self.view.comboBoxUFZonaEntrega.current_text
        taxa = self.view.doubleSpinBoxTaxaZonaEntrega.value

        body = {
            "nome": nome,
            "cidade": cidade,
            "uf": UF,
            "bairro": Bairro,
            "cep": CEP,
            "taxa_de_entrega": taxa,
            "loja_uuid": self.loja.uuid,
        }

        response = self.post_request("zonas-de-entrega/", json=body)

        try:
            self.handle_response(
                response, "Zona de entrega cadastrada com sucesso!"
            )  # ####
        except ValueError:
            return None

        self.view.lineEditNomeZonaEntrega.clear()
        self.view.lineEditCidadeZonaEntrega.clear()
        self.view.lineEditBairroZonaEntrega.clear()
        self.view.lineEditCEPZonaEntrega.clear()
"""
