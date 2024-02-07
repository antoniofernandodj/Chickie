from src.custom_widgets import CustomTableWidgetItem
from typing import Optional, List
from datetime import datetime
from contextlib import suppress
from unidecode import unidecode
from PySide6.QtCore import (
    Signal,
    Slot,
    Qt
)
from PySide6.QtWidgets import (
    QMessageBox,
    QTableWidgetItem,
    QTableWidget,
    QFileDialog,
    QWidget,
    QVBoxLayout,
    QRadioButton
)

from src.domain.services import (
    AuthService,
    ProdutoService,
    CategoriaService,
    PedidoService,
    PrecoService,
    StatusService,
    IngredienteService
)

from src.domain.data_models import ItemPedidoPOST
from src.services import FileService

from src.ui_models import PrecosModel, ProdutosModel, IngredienteModel
from __feature__ import snake_case, true_property  # type: ignore  # noqa
import os

from src.custom_widgets.ingrediente_group_ui import (
    get_ingrediente_group
)

from src.domain.data_models import (  # noqa
    Produto,
    Preco,
    Status,
    Ingrediente,
    ProdutoPOST,
    CategoriaProdutos,
    Funcionario,
    ZonaDeEntrega,
    Pedido,
    PedidoPOST,
    ItemPedido,
    EnderecoEntrega,
    IngredientesSelect
)

from src.controllers.base import BaseController

with suppress(ImportError):
    from src.windows import MainWindow
    from src.views.main_ui import Ui_MainWindow as MainView


class IngredientesContainer(QWidget):

    data: List[Ingrediente]
    select: dict[str, bool]

    def setup(self) -> None:
        self.data = []
        self.select = {}

    def add_data(self, ingrediente: Ingrediente):
        self.data.append(ingrediente)

    def get_data(self):
        return self.data


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
        self.pedido_service = PedidoService()
        self.preco_service = PrecoService()
        self.status_service = StatusService()
        self.ingrediente_service = IngredienteService()
        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup()

        self.produto_model = ProdutosModel(self.window)
        self.preco_model = PrecosModel(self.window)
        self.ingrediente_model = IngredienteModel(self.window)

        self.total_pedido = 0.0

    def radio_clicked(self):
        radio_button: QRadioButton = self.sender()  # type: ignore
        ingrediente: Ingrediente = radio_button.ingrediente  # type: ignore
        self.ingrediente_container.select[str(ingrediente.uuid)] = (
            radio_button.checked
        )

    def adicionar_ingrediente(
        self,
        container_widget: QWidget,
        label: str,
        data: Ingrediente
    ) -> None:

        qss_path = 'src/styles/ingrediente.qss'
        qss = FileService.get_text(qss_path)
        container_widget.style_sheet = qss
        layout = container_widget.layout()

        IngredienteGroup = get_ingrediente_group(label=label)
        ui = IngredienteGroup()
        ui.setupUi(container_widget)
        ui.radio_nao.ingrediente = data  # type: ignore
        ui.radio_sim.ingrediente = data  # type: ignore

        ui.radio_nao.clicked.connect(self.radio_clicked)
        ui.radio_sim.clicked.connect(self.radio_clicked)

        layout.add_widget(ui.frame)

    def setup(self):
        self.loja = self.auth_service.get_loja_data()

        self.view.table_widget_item_pedido.row_count = 0

        # Let's register callbacks!!!

        cb = self.show_file_dialog
        self.view.push_button_escolher_imagem_produto.clicked.connect(cb)

        cb = self.remover_item_na_lista
        self.view.table_widget_item_pedido.itemDoubleClicked.connect(cb)

        cb = self.refresh_precos
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

        cb = self.refresh_ingredientes
        self.view.combo_box_item_pedido.currentIndexChanged.connect(cb)

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

    def refresh_ingredientes(self, item) -> None:
        produto: Produto = self.view.combo_box_item_pedido.current_data()
        if produto.uuid is None:
            raise
        ingredientes = self.ingrediente_model.get_data(produto.uuid)

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup()

        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.set_layout(container_layout)

        for ingrediente in ingredientes:
            self.ingrediente_container.add_data(ingrediente)
            self.adicionar_ingrediente(
                self.ingrediente_container,
                ingrediente.nome,
                ingrediente
            )

        parent.set_widget(self.ingrediente_container)
        parent.widget_resizable = True

    def show_file_dialog(self):
        label = self.view.label_produto_image_filename

        formats = [
            'Images [png, jpg, jpeg, bmp, gif] (*.png *.jpg *.jpeg *.bmp *.gif)',  # noqa
            'PNG (*.png)',
            'JPG (*.jpg)',
            'JPEG (*.jpeg)',
            'bitmap (*.bmp)',
            'GIF (*.gif)'
        ]
        filters = ';;'.join(formats)
        caption = 'Escolha a imagem'
        file_path, _ = QFileDialog.get_open_file_name(
            self.window,
            filter=filters,
            selectedFilter=formats[0],
            caption=caption
        )
        if len(file_path) > 60:
            label.text = f"...{file_path[-60:]}"
        else:
            label.text = f"...{file_path}"
        label.value = file_path  # type: ignore  # noqa

    def set_frete_spin_box(self):
        if self.view.check_box_frete_pedido.checked:  # type: ignore
            self.view.double_spin_box_frete_pedido.hide()
        else:
            self.view.double_spin_box_frete_pedido.show()

    def refresh_text_browser_total_pedido(self):
        fmt = f"R${self.total_pedido:.2f}"
        self.view.line_edit_total_item_pedido.text = fmt

    def get_table_selected_row_items(self, table_widget: QTableWidget):
        items_in_row = []

        selected_row = table_widget.current_row()
        for col in range(table_widget.column_count):
            item: CustomTableWidgetItem = table_widget.item(  # type: ignore
                selected_row, col
            )
            if item:
                items_in_row.append(item.get_stored_data())

        return items_in_row

    def remover_item_na_lista(self, item: QTableWidgetItem) -> None:
        table_widget = self.view.table_widget_item_pedido

        selected_row = table_widget.current_row()

        items_in_row = self.get_table_selected_row_items(table_widget)

        preco = items_in_row[1]
        quantidade = items_in_row[2]
        if not isinstance(preco, float) or not isinstance(quantidade, int):
            raise TypeError('Tipos inválidos')

        subtotal = preco * quantidade

        if selected_row >= 0:
            table_widget.remove_row(selected_row)

        self.total_pedido -= subtotal
        self.refresh_text_browser_total_pedido()

    def adicionar_item_na_lista(self) -> None:
        table_widget = self.view.table_widget_item_pedido
        combo_box = self.view.combo_box_item_pedido
        produto: Optional[Produto] = combo_box.current_data()

        if produto is None or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.critical(self.window, title, message)
            return

        quantidade = self.view.spin_box_item_pedido.value
        subtotal = produto.preco * quantidade

        ingredientes: List[IngredientesSelect] = []
        for uuid, value in self.ingrediente_container.select.items():
            select = IngredientesSelect(uuid=uuid, value=value)
            ingredientes.append(select)

        ip = ItemPedidoPOST(
            quantidade=self.view.spin_box_item_pedido.value,
            observacoes=self.view.text_edit_observacao_item.plain_text,
            produto_uuid=produto.uuid,
            ingredientes=ingredientes,
            loja_uuid=self.loja.uuid
        )

        ingredientes_nomes: list[str] = []

        for ingrediente_sel in ip.ingredientes:
            if ingrediente_sel.value is True:
                uuid = ingrediente_sel.uuid
                ingrediente = self.ingrediente_service.get(uuid)
                ingredientes_nomes.append(ingrediente.nome)

        row_count = table_widget.row_count
        table_widget.insert_row(row_count)

        datas = [
            (produto.nome, produto.uuid),
            (produto.preco, produto.preco),
            (ip.quantidade, ip.quantidade),
            (produto.preco * ip.quantidade, produto.preco * ip.quantidade),
            (ip.observacoes, ip.observacoes),
            (', '.join(ingredientes_nomes), ip.ingredientes)
        ]

        row: List[CustomTableWidgetItem] = []
        for data in datas:
            item = CustomTableWidgetItem(str(data[0]))
            item.store_data(data[1])
            row.append(item)

        for column, item in enumerate(row):
            item.set_flags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            table_widget.set_item(row_count, column, item)

        self.total_pedido += subtotal
        self.refresh_text_browser_total_pedido()

        self.view.text_edit_observacao_item.clear()
        self.view.spin_box_item_pedido.value = 1
        self.view.spin_box_quantidade_acicionais.value = 0

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup()
        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.set_layout(container_layout)
        parent.set_widget(self.ingrediente_container)
        parent.widget_resizable = True

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
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None

        title = 'Sucesso'
        message = "Categoria de produto cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

        self.view.line_edit_nome_categoria_produto.clear()
        self.view.plain_text_edit_descricao_categoria_produto.clear()
        self.categoria_catastrada.emit(categoria)

    def cadastrar_produto(self) -> None:
        label = self.view.label_produto_image_filename
        file_path: str = label.value  # type: ignore

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
            image_bytes=FileService.get_base64_string(file_path),
            filename=os.path.basename(label.text)
        )

        response = self.produto_service.save(produto)

        try:
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None

        title = 'Sucesso'
        message = "Produto cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

        self.view.line_edit_nome_produto.clear()
        self.view.text_edit_descricao_produto.clear()
        self.view.double_spin_box_preco_produto.clear()
        self.produto_catastrado.emit(produto)
        label.clear()

    def cadastrar_preco(self):
        produto = self.view.combo_box_produto_preco.current_data()

        valor = self.view.double_spin_valor_preco.value
        combo = self.view.combo_box_dia_da_semana_preco
        dia_da_semana = unidecode(combo.current_text[:3].lower())

        if produto is None or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.critical(self.window, title, message)
            return

        response = self.preco_service.save(Preco(
            produto_uuid=produto.uuid,
            valor=valor,
            dia_da_semana=dia_da_semana,
        ))

        try:
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None

        title = 'Sucesso'
        message = "Preço de produto cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

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
            "nome": nome,
            "username": username,
            "email": email,
            "telefone": telefone,
            "celular": celular,
            "endereco": {
                "uf": uf,
                "cidade": cidade,
                "logradouro": logradouro,
                "numero": numero,
                "nome": nome,
                "complemento": complemento,
                "bairro": bairro,
                "cep": cep,
            },
            "password": senha,
            "loja_uuid": self.loja.uuid,
        }

        response = self.post_request("loja/cliente", json=body)

        try:
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None

        title = 'Sucesso'
        message = "Cliente cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

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

    def get_itens_pedido(self) -> List[ItemPedidoPOST]:
        items_pedido: List[ItemPedidoPOST] = []
        table_widget = self.view.table_widget_item_pedido
        for row_number in range(table_widget.row_count):
            row_items = []
            for column_number in range(table_widget.column_count):
                item: CustomTableWidgetItem = (  # type: ignore
                    table_widget.item(row_number, column_number)
                )
                item_data = item.get_stored_data()
                row_items.append(item_data)

            items_pedido.append(ItemPedidoPOST(
                produto_uuid=row_items[0],
                quantidade=row_items[2],
                observacoes=row_items[4],
                ingredientes=row_items[5],
            ))

        return items_pedido

    def cadastrar_pedido(self):
        items_pedido = self.get_itens_pedido()
        frete = self.view.double_spin_box_frete_pedido.value
        cep = self.view.line_edit_cep.text
        celular = self.view.line_edit_celular_pedido.text
        cidade = self.view.line_edit_cidade.text
        logradouro = self.view.line_edit_logradouro_pedido.text
        uf = self.view.combo_box_uf_pedido.current_text
        numero = self.view.line_edit_numero_end.text
        bairro = self.view.line_edit_bairro.text
        complemento = self.view.line_edit_complemento.text
        comentarios = self.view.text_edit_comentarios_pedido.plain_text

        pedido = PedidoPOST(
            celular=celular,
            data_hora=datetime.now().isoformat(),
            endereco=EnderecoEntrega(
                uf=uf,
                cidade=cidade,
                logradouro=logradouro,
                numero=numero,
                bairro=bairro,
                cep=cep,
                complemento=complemento,
            ),
            frete=frete,
            itens=items_pedido,
            loja_uuid=self.loja.uuid,
            comentarios=comentarios
        )

        print({'pedido': pedido})

        # response = self.pedido_service.save(pedido)

        # try:
        #     self.handle_response(response)
        # except ValueError as error:
        #     self.show_message('Error', str(error))
        #     return

        title = 'Sucesso'
        message = 'Pedido cadastrado com sucesso!'
        QMessageBox.information(self.window, title, message)

        self.view.line_edit_cep.clear()
        self.view.line_edit_celular_pedido.clear()
        self.view.line_edit_cidade.clear()
        self.view.line_edit_logradouro_pedido.clear()
        self.view.line_edit_numero_end.clear()
        self.view.line_edit_bairro.clear()
        self.view.line_edit_complemento.clear()
        self.view.text_edit_comentarios_pedido.clear()
        self.view.text_edit_observacao_item.clear()
        self.view.double_spin_box_frete_pedido.value = 0
        self.view.table_widget_item_pedido.row_count = 0

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup()
        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.set_layout(container_layout)
        parent.set_widget(self.ingrediente_container)
        parent.widget_resizable = True

    def cadastrar_status_pedido(self):
        nome = self.view.line_edit_nome_status_pedido.text
        descricao = self.view.text_edit_descricao_status_pedido.plain_text

        response = self.status_service.save(Status(
            nome=nome,
            descricao=descricao,
            loja_uuid=self.loja.uuid
        ))

        try:
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None

        title = 'Sucesso'
        message = "Status de pedido cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

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

    def refresh_precos(self) -> None:
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
