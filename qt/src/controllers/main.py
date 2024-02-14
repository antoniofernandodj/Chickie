from os import path
import httpx
from src.config import settings  # type: ignore
from src.controllers.base import BaseController
from src.domain.data_models import ItemPedidoPOST
from src.services import FileService
from typing import Optional, List, Any
from datetime import datetime
from contextlib import suppress
from unidecode import unidecode
from dataclasses import dataclass
from src.components import (
    CustomTableWidgetItem,
    IngredientesContainer,
    IngredienteGroup,
    CustomRadioButton
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMessageBox,
    QTableWidget,
    QFileDialog,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtGui import QPixmap
from src.domain.services import (
    AuthService,
    ProdutoService,
    CategoriaService,
    PedidoService,
    PrecoService,
    StatusService,
    IngredienteService
)
from src.ui_models import (
    DiasDisponiveisListModel,
    PrecosDeProdutoListModel,
    StatusListModel,
    CategoriaListModel,
    ProdutosListModel,
    IngredientesListModel
)
from src.domain.data_models import (
    Preco,
    Status,
    Ingrediente,
    ProdutoPOST,
    ProdutoGET,
    CategoriaProdutos,
    PedidoPOST,
    EnderecoEntrega,
    IngredientesSelect
    # Funcionario,
    # ZonaDeEntrega,
    # Pedido,
    # ItemPedido,
)


@dataclass
class Data:
    name: str
    value: Any


with suppress(ImportError):
    from src.windows import MainWindow
    from src.views.main_ui import Ui_MainWindow as MainView


class MainController(BaseController):

    def __init__(self, view: "MainView", app, window: "MainWindow"):
        super().__init__()

        self.view = view
        self.app = app
        self.window = window

        self.auth_service = AuthService()
        self.preco_service = PrecoService()
        self.status_service = StatusService()
        self.pedido_service = PedidoService()
        self.produto_service = ProdutoService()
        self.categoria_service = CategoriaService()
        self.ingrediente_service = IngredienteService()

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)

        w = self.window
        self.ingrediente_list_model = IngredientesListModel(w)
        self.produtos_model = ProdutosListModel(None, w)
        self.precos_model = PrecosDeProdutoListModel(None, w)
        self.dias_disponiveis_model = (
            DiasDisponiveisListModel(None, w)
        )
        self.categoria_model = CategoriaListModel(w)
        self.status_model = StatusListModel(w)
        c = self.categoria_model
        d = self.dias_disponiveis_model
        self.view.combo_box_categorias_preco.setModel(c)
        self.view.combo_box_categoria_produto.setModel(c)
        self.view.list_view_categorias_cadastradas.setModel(c)
        self.view.combo_box_item_pedido.setModel(self.produtos_model)
        self.view.combo_box_produto_preco.setModel(self.produtos_model)
        self.view.combo_box_dia_da_semana_preco.setModel(d)
        self.view.list_view_status_cadastrados.setModel(self.status_model)
        self.view.list_view_precos_cadastrados.setModel(self.precos_model)
        self.view.list_view_ingredientes.setModel(self.ingrediente_list_model)
        self.view.list_view_produtos_cadastrados.setModel(self.produtos_model)
        self.view.combo_box_categoria_pedido.setModel(self.categoria_model)
        self.view.action_pedidos.triggered.connect(self.visualizar_pedidos)
        self.view.action_historico.triggered.connect(self.visualizar_historico)

        self.total_pedido = 0.0

        self.refresh_ingredientes()

    def visualizar_pedidos(self):
        from src.windows import PedidosDialog

        dialog_pedidos = PedidosDialog()
        dialog_pedidos.show()

    def visualizar_historico(self):
        from src.windows import HistoricoDialog

        dialog_historico = HistoricoDialog()
        dialog_historico.show()

    def radio_ingrediente_clicked(self) -> None:
        radio_button: CustomRadioButton = self.sender()  # type: ignore
        ingrediente = radio_button.get_ingrediente()
        value = radio_button.get_value()
        self.ingrediente_container.select[str(ingrediente.uuid)] = value

    def adicionar_ingrediente_a_pedido(
        self,
        container_widget: QWidget,
        label: str,
        ingrediente: Ingrediente
    ) -> None:

        if settings.STYLES:
            qss_path = 'src/styles/ingrediente.qss'
            qss = FileService.get_text(qss_path)
            container_widget.setStyleSheet(qss)

        layout = container_widget.layout()

        ui = IngredienteGroup()
        ui.setup_ui(label, container_widget)

        for button in [ui.radio_nao, ui.radio_sim]:
            button.set_ingrediente(ingrediente)
            button.clicked.connect(self.radio_ingrediente_clicked)

        layout.addWidget(ui.frame)

    def adicionar_ingrediente_a_lista_de_cadastro(self):
        nome = self.view.line_edit_nome_ingrediente.text()
        descricao = self.view.text_edit_ingrediente_descricao.toPlainText()
        ingrediente = {'nome': nome, 'descricao': descricao}

        self.ingrediente_list_model.add_ingrediente(ingrediente)

        self.view.line_edit_nome_ingrediente.clear()
        self.view.text_edit_ingrediente_descricao.clear()

    def remover_ingrediente_da_lista_de_cadastro(self):
        selected_items = self.view.list_view_ingredientes.selectedIndexes()
        if selected_items:
            item = selected_items[0]
            self.ingrediente_list_model.remove(item)

    def setup(self) -> None:
        self.loja = self.auth_service.get_loja_data()

        self.view.table_widget_item_pedido.setRowCount(0)

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

        cb = self.cadastrar_pedido
        self.view.push_button_cadastrar_pedido.clicked.connect(cb)

        cb = self.cadastrar_status_pedido
        self.view.push_button_cadastrar_status_pedido.clicked.connect(cb)

        cb = self.adicionar_item_na_lista
        self.view.push_button_adicionar_item_pedido.clicked.connect(cb)

        cb = self.refresh_ingredientes
        self.view.combo_box_item_pedido.currentIndexChanged.connect(cb)

        cb = self.itens_pedido_refresh
        self.view.combo_box_categoria_pedido.currentIndexChanged.connect(cb)

        cb = self.refresh_produtos
        self.view.combo_box_categoria_produto.currentIndexChanged.connect(cb)

        cb = self.refresh_produtos_preco
        self.view.combo_box_categorias_preco.currentIndexChanged.connect(cb)

        cb = self.remover_produto
        self.view.push_button_remover_produto.clicked.connect(cb)

        cb = self.remover_preco
        self.view.push_button_remover_preco.clicked.connect(cb)

        cb = self.remover_categoria
        self.view.push_button_remover_categoria.clicked.connect(cb)

        cb = self.remover_status
        self.view.push_button_remover_status.clicked.connect(cb)

        cb = self.adicionar_ingrediente_a_lista_de_cadastro
        self.view.push_button_adicionar_ingrediente.clicked.connect(cb)

        cb = self.remover_ingrediente_da_lista_de_cadastro
        self.view.push_button_remover_ingrediente.clicked.connect(cb)

        # cb = self.cadastrar_cliente
        # self.view.push_button_cadastrar_cliente.clicked.connect(cb)

        # self.view.pushButtonCadastrarFornecedor.clicked.connect(
        #     self.cadastrar_fornecedor
        # )
        # self.view.pushButtonCadastrarFuncionario.clicked.connect(
        #     self.cadastrar_funcionario
        # )
        # self.view.pushButtonCadastrarZonaEntrega.clicked.connect(
        #     self.cadastrar_zona_entrega
        # )

    def remover_preco(self) -> None:

        QMB = QMessageBox
        title = 'Confirmar'
        text = 'Você tem certeza que deseja remover o preço selecionado?'
        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        selected_items = (
            self.view.list_view_precos_cadastrados.selectedIndexes()
        )

        if selected_items:
            try:
                preco_index = selected_items[0]
            except Exception:
                return

            try:
                preco_removido = self.precos_model.remove(preco_index)
                produto_uuid = preco_removido.produto_uuid
                self.dias_disponiveis_model.refresh(produto_uuid)

                title = 'Sucesso'
                message = 'Preco removido com sucesso!'
                QMessageBox.information(self.window, title, message)
            except Exception:
                title = 'Erro'
                message = 'Erro na remoção do preço!'
                QMessageBox.critical(self.window, title, message)
                return

    def remover_produto(self) -> None:
        QMB = QMessageBox
        title = 'Confirmar'
        text = ('Você tem certeza que deseja remover o produto '
                'e todos os preços associados?')

        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        selected_indexes = (
            self.view.list_view_produtos_cadastrados.selectedIndexes()
        )

        if selected_indexes is None:
            return

        selected_index = selected_indexes[0]

        produto_uuid = self.produtos_model.data(
            selected_index,
            role=Qt.ItemDataRole.UserRole
        )

        if produto_uuid is None:
            return

        produto = self.produto_service.get(produto_uuid)
        if not isinstance(produto, ProdutoGET):
            raise

        status_code = self.produto_service.delete_by_uuid(produto_uuid)
        if status_code is None or not (200 <= status_code < 300):
            QMessageBox.information(self.window, 'Erro', (
                'Erro na remoção do produto. '
            ))
            return

        title = 'Sucesso'
        message = 'Produto removido com sucesso!'
        QMessageBox.information(self.window, title, message)
        self.produtos_model.refresh(produto.categoria_uuid)

    def remover_categoria(self) -> None:
        QMB = QMessageBox
        title = 'Confirmar'
        text = ('Você tem certeza que deseja remover a categoria '
                'selecionada?')

        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        selected_indexes = (
            self.view.list_view_categorias_cadastradas.selectedIndexes()
        )

        if selected_indexes is None:
            return

        selected_index = selected_indexes[0]

        categoria_uuid = self.categoria_model.data(
            selected_index,
            role=Qt.ItemDataRole.UserRole
        )

        if categoria_uuid is None:
            return

        status_code = self.categoria_service.delete_by_uuid(categoria_uuid)
        if status_code is None or not (200 <= status_code < 300):
            QMessageBox.warning(self.window, 'Erro', (
                'Erro na remoção da categoria. '
                'verifique se a mesma não possui produtos associados'
            ))
            return

        title = 'Sucesso'
        message = 'Categoria removida com sucesso!'
        QMessageBox.information(self.window, title, message)
        self.categoria_model.refresh()

    def remover_status(self) -> None:
        QMB = QMessageBox
        title = 'Confirmar'
        text = ('Você tem certeza que deseja remover o status '
                'selecionado?')

        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        selected_indexes = (
            self.view.list_view_status_cadastrados.selectedIndexes()
        )

        if selected_indexes is None:
            return

        selected_index = selected_indexes[0]

        status_uuid = self.status_model.data(
            selected_index,
            role=Qt.ItemDataRole.UserRole
        )

        if status_uuid is None:
            return

        status_code = self.status_service.delete_by_uuid(status_uuid)
        if status_code is None or not (200 <= status_code < 300):
            QMessageBox.warning(self.window, 'Erro', (
                'Erro na remoção do Status. '
                'verifique se o mesmo não possui pedidos associados'
            ))
            return

        title = 'Sucesso'
        message = 'Status removida com sucesso!'
        QMessageBox.information(self.window, title, message)
        self.status_model.refresh()

    def itens_pedido_refresh(self) -> None:
        self.view.label_image.setPixmap(QPixmap())
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)
        self.view.list_widget_adicionais_pedido.clear()
        categoria_uuid = self.view.combo_box_categoria_pedido.currentData()
        self.produtos_model.refresh(categoria_uuid)

    def refresh_produtos_preco(self) -> None:
        model = self.produtos_model
        model.clear()

        categoria_uuid = self.view.combo_box_categorias_preco.currentData()
        self.produtos_model.refresh(categoria_uuid)

    def refresh_produtos(self) -> None:
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)
        self.view.list_widget_adicionais_pedido.clear()

        categoria_uuid = self.view.combo_box_categoria_produto.currentData()
        self.produtos_model.refresh(categoria_uuid)

    def refresh_ingredientes(self) -> None:
        self.view.label_image.setPixmap(QPixmap())
        self.view.list_widget_adicionais_pedido.clear()

        produto_uuid: str = self.view.combo_box_item_pedido.currentData()
        produto = self.produto_service.get(produto_uuid)
        if isinstance(produto, ProdutoGET):
            response = httpx.get(produto.image_url or '')
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                self.view.label_image.setPixmap(pixmap)

        if produto_uuid is None:
            scroll_area = self.view.scroll_area_ingredientes
            self.ingrediente_container.setup(scroll_area)
            self.view.list_widget_adicionais_pedido.clear()
            return

        ingredientes = self.ingrediente_service.get_all({
            'produto_uuid': produto_uuid
        })

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)

        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.setLayout(container_layout)

        for ingrediente in ingredientes:
            self.ingrediente_container.add_data(ingrediente)
            self.adicionar_ingrediente_a_pedido(
                self.ingrediente_container,
                ingrediente.nome,
                ingrediente
            )

            self.ingrediente_container.select[ingrediente.uuid] = None

        parent.setWidget(self.ingrediente_container)
        parent.setWidgetResizable(True)

    def show_file_dialog(self) -> None:
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
        file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            filter=filters,
            selectedFilter=formats[0],
            caption=caption
        )
        if len(file_path) > 60:
            label.setText(f"...{file_path[-60:]}")
        else:
            label.setText(f"...{file_path}")
        label.value = file_path  # type: ignore  # noqa

    def refresh_text_browser_total_pedido(self) -> None:
        fmt = f"R${self.total_pedido:.2f}"
        self.view.line_edit_total_item_pedido.setText(fmt)

    def get_table_selected_row_items(self, table_widget: QTableWidget):
        items_in_row = []

        selected_row = table_widget.currentRow()
        for col in range(table_widget.columnCount()):
            item: CustomTableWidgetItem = table_widget.item(  # type: ignore
                selected_row, col
            )
            if item:
                items_in_row.append(item.get_stored_data())

        return items_in_row

    def remover_item_na_lista(self) -> None:
        table_widget = self.view.table_widget_item_pedido

        selected_row = table_widget.currentRow()

        items_in_row = self.get_table_selected_row_items(table_widget)

        preco = items_in_row[1]
        quantidade = items_in_row[2]
        if not isinstance(preco, float) or not isinstance(quantidade, int):
            raise TypeError('Tipos inválidos')

        subtotal = preco * quantidade

        if selected_row >= 0:
            table_widget.removeRow(selected_row)

        self.total_pedido -= subtotal
        self.refresh_text_browser_total_pedido()

    def adicionar_item_na_lista(self) -> None:
        table_widget = self.view.table_widget_item_pedido
        combo_box = self.view.combo_box_item_pedido
        produto_uuid: str = combo_box.currentData()

        produto = self.produto_service.get(produto_uuid)
        if not isinstance(produto, ProdutoGET) or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.warning(self.window, title, message)
            return

        quantidade = self.view.spin_box_item_pedido.value()
        subtotal = produto.preco * quantidade

        ingredientes: List[IngredientesSelect] = []
        for uuid, value in self.ingrediente_container.select.items():
            if value is None:
                title = 'Aviso'
                message = 'Favor, marcar todos os ingredientes!'
                QMessageBox.warning(self.window, title, message)
                return

            if value is True:
                select = IngredientesSelect(uuid=uuid, value=value)
                ingredientes.append(select)

        ip = ItemPedidoPOST(
            quantidade=self.view.spin_box_item_pedido.value(),
            observacoes=self.view.text_edit_observacao_item.toPlainText(),
            produto_uuid=produto.uuid,
            ingredientes=ingredientes,
            loja_uuid=self.loja.uuid
        )

        ingredientes_nomes: list[str] = []

        for ingrediente_sel in ip.ingredientes:
            if ingrediente_sel.value is True:
                uuid = ingrediente_sel.uuid
                ingrediente = self.ingrediente_service.get(uuid)
                if not isinstance(ingrediente, Ingrediente):
                    raise
                ingredientes_nomes.append(ingrediente.nome)

        row_count = table_widget.rowCount()
        table_widget.insertRow(row_count)

        subtotal = produto.preco * ip.quantidade
        preco = produto.preco

        datas: list[Data] = [
            Data(name=produto.nome, value=produto.uuid),
            Data(name=f'R${preco:.2f}'.replace('.', ','), value=preco),
            Data(name=str(ip.quantidade), value=ip.quantidade),
            Data(name=f'R${subtotal:.2f}'.replace('.', ','), value=subtotal),
            Data(name=ip.observacoes, value=ip.observacoes),
            Data(name=', '.join(ingredientes_nomes), value=ip.ingredientes)
        ]

        row: List[CustomTableWidgetItem] = []
        for data in datas:
            item = CustomTableWidgetItem(data.name)
            item.store_data(data.value)
            row.append(item)

        for column_number, item in enumerate(row):
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            table_widget.setItem(row_count, column_number, item)

        self.total_pedido += subtotal
        self.refresh_text_browser_total_pedido()

        self.view.text_edit_observacao_item.clear()
        self.view.spin_box_item_pedido.setValue(1)
        self.view.spin_box_quantidade_acicionais.setValue(0)

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)
        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.setLayout(container_layout)
        parent.setWidget(self.ingrediente_container)
        parent.setWidgetResizable(True)

    def cadastrar_categoria_produto(self) -> None:
        text_edit = self.view.text_edit_descricao_categoria_produto

        nome = self.view.line_edit_nome_categoria_produto.text()
        descricao = text_edit.toPlainText()

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
        self.view.text_edit_descricao_categoria_produto.clear()

        self.categoria_model.refresh()

    def cadastrar_produto(self) -> None:
        QMB = QMessageBox
        title = 'Confirmar'
        text = ('Tem certeza que deseja cadastrar o produto '
                'com as informações escolhidas?')

        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        label = self.view.label_produto_image_filename
        try:
            file_path: str = label.value  # type: ignore
        except AttributeError:
            title = 'Alerta'
            message = 'Escolher imagem de produto!'
            QMessageBox.warning(self.window, title, message)
            return

        nome = self.view.line_edit_nome_produto.text()
        produto_descricao = self.view.text_edit_descricao_produto.toPlainText()

        categoria_uuid: Optional[str] = (
            self.view.combo_box_categoria_produto.currentData()
        )
        if categoria_uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos uma categoria!'
            QMessageBox.warning(self.window, title, message)
            return

        preco = self.view.double_spin_box_preco_produto.value()

        produto = ProdutoPOST(
            nome=nome,
            descricao=produto_descricao,
            categoria_uuid=categoria_uuid,
            loja_uuid=self.loja.uuid,
            preco=preco,
            image_bytes=FileService.get_base64_string(file_path),
            filename=path.basename(file_path)
        )

        response = self.produto_service.save(produto)

        try:
            produto_uuid = self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return None
        if produto_uuid is None:
            self.show_message('Error', 'Erro no cadastro do produto')
            return None

        ingredientes_error: List[Ingrediente] = []
        for ingrediente_data in self.ingrediente_list_model.ingredientes():
            ingrediente = Ingrediente(
                nome=ingrediente_data['nome'],
                descricao=ingrediente_data['descricao'],
                produto_uuid=produto_uuid,
                loja_uuid=self.loja.uuid
            )
            response = self.ingrediente_service.save(ingrediente)
            if (600 > response.status_code >= 400):
                ingredientes_error.append(ingrediente)

        for i in ingredientes_error:
            title = 'Erro'
            message = f"Erro no cadastrado do ingrediente {i.nome}!"
            QMessageBox.critical(self.window, title, message)

        title = 'Sucesso'
        message = "Produto cadastrado com sucesso!"
        QMessageBox.information(self.window, title, message)

        self.view.line_edit_nome_produto.clear()
        self.view.text_edit_descricao_produto.clear()
        self.view.double_spin_box_preco_produto.clear()
        self.view.line_edit_nome_ingrediente.clear()
        self.view.text_edit_ingrediente_descricao.clear()

        self.produtos_model.refresh(categoria_uuid)
        self.ingrediente_list_model.clear()

        label.clear()

    def cadastrar_preco(self) -> None:
        combo_box = self.view.combo_box_dia_da_semana_preco
        spinbox = self.view.double_spin_valor_preco

        produto_uuid = self.view.combo_box_produto_preco.currentData()
        if produto_uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.warning(self.window, title, message)
            return

        produto: Optional[ProdutoGET] = self.produto_service.get(produto_uuid)

        valor = self.view.double_spin_valor_preco.value()
        combo = self.view.combo_box_dia_da_semana_preco
        dia_da_semana = unidecode(combo.currentText()[:3].lower())

        if produto is None or produto.uuid is None:
            title = 'Aviso'
            message = 'Escolha ao menos um produto!'
            QMessageBox.warning(self.window, title, message)
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

        spinbox.setValue(0)

        combo_box.removeItem(combo_box.currentIndex())

        self.precos_model.refresh(produto.uuid)
        self.dias_disponiveis_model.refresh(produto.uuid)

    def get_itens_pedido(self) -> List[ItemPedidoPOST]:

        items_pedido: List[ItemPedidoPOST] = []

        table_widget = self.view.table_widget_item_pedido
        for row_number in range(table_widget.rowCount()):
            row_items = []
            for column_number in range(table_widget.columnCount()):
                item: CustomTableWidgetItem = (  # type: ignore
                    table_widget.item(row_number, column_number)
                )
                item_data = item.get_stored_data()

                row_items.append(item_data)

            # 0: uuid
            # 1: preco
            # 2: quantidade
            # 3: subtotal
            # 4: observacoes
            # 5: ingredientes
            items_pedido.append(ItemPedidoPOST(
                produto_uuid=row_items[0],
                quantidade=row_items[2],
                observacoes=row_items[4],
                ingredientes=row_items[5],
            ))

        return items_pedido

    def cadastrar_pedido(self) -> None:
        QMB = QMessageBox
        title = 'Confirmar'
        text = ('Tem certeza que deseja cadastrar o pedido '
                'com as informações escolhidas?')

        buttons = QMB.StandardButton.Yes | QMB.StandardButton.No
        confirm = QMB.question(self.window, title, text, buttons)
        if confirm == QMB.StandardButton.No:
            return

        items_pedido = self.get_itens_pedido()
        if len(items_pedido) == 0:
            title = 'Aviso'
            text = 'Escolher ao menos um item no pedido!'
            QMessageBox.warning(self.window, title, text)
            return None

        frete = self.view.double_spin_box_frete_pedido.value()
        cep = self.view.line_edit_cep.text()
        celular = self.view.line_edit_celular_pedido.text()
        cidade = self.view.line_edit_cidade.text()
        logradouro = self.view.line_edit_logradouro_pedido.text()
        uf = self.view.combo_box_uf_pedido.currentText()
        numero = self.view.line_edit_numero_end.text()
        bairro = self.view.line_edit_bairro.text()
        complemento = self.view.line_edit_complemento.text()
        comentarios = self.view.text_edit_comentarios_pedido.toPlainText()

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

        response = self.pedido_service.save(pedido)

        try:
            self.handle_response(response)
        except ValueError as error:
            self.show_message('Error', str(error))
            return

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
        self.view.double_spin_box_frete_pedido.setValue(0)
        self.view.table_widget_item_pedido.setRowCount(0)

        self.view.label_image.setPixmap(QPixmap())
        self.view.list_widget_adicionais_pedido.clear()
        scroll_area = self.view.scroll_area_ingredientes
        self.ingrediente_container.setup(scroll_area)

        self.view.combo_box_categoria_pedido.setCurrentIndex(0)
        self.produtos_model.refresh()

        parent = self.view.scroll_area_ingredientes

        self.ingrediente_container = IngredientesContainer()
        self.ingrediente_container.setup(self.view.scroll_area_ingredientes)
        container_layout = QVBoxLayout(self.ingrediente_container)
        self.ingrediente_container.setLayout(container_layout)
        parent.setWidget(self.ingrediente_container)
        parent.setWidgetResizable(True)

    def cadastrar_status_pedido(self) -> None:
        nome = self.view.line_edit_nome_status_pedido.text()
        descricao = self.view.text_edit_descricao_status_pedido.toPlainText()

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

        self.status_model.refresh()

    def refresh_precos(self) -> None:
        combo_box = self.view.combo_box_produto_preco
        produto_uuid: str = combo_box.currentData()

        self.precos_model.refresh(produto_uuid)
        self.dias_disponiveis_model.refresh(produto_uuid)

    # def cadastrar_cliente(self):
    #     nome = self.view.line_edit_nome_cliente.text
    #     email = self.view.line_edit_email_cliente.text
    #     username = self.view.line_edit_username_cliente.text
    #     telefone = self.view.line_edit_telefone_cliente.text
    #     celular = self.view.line_edit_celular_cliente.text
    #     senha = '123456'

    #     logradouro = self.view.line_edit_logradouro_cliente.text
    #     uf = self.view.combo_box_uf_cliente.currentText()
    #     cidade = self.view.line_edit_cidade_cliente.text
    #     numero = self.view.line_edit_numero_cliente.text
    #     bairro = self.view.line_edit_bairro_cliente.text
    #     cep = self.view.line_edit_cep_cliente.text
    #     complemento = self.view.line_edit_complemento_cliente.text

    #     body = {
    #         "nome": nome,
    #         "username": username,
    #         "email": email,
    #         "telefone": telefone,
    #         "celular": celular,
    #         "endereco": {
    #             "uf": uf,
    #             "cidade": cidade,
    #             "logradouro": logradouro,
    #             "numero": numero,
    #             "nome": nome,
    #             "complemento": complemento,
    #             "bairro": bairro,
    #             "cep": cep,
    #         },
    #         "password": senha,
    #         "loja_uuid": self.loja.uuid,
    #     }

    #     # try:
    #     #     self.handle_response(response)
    #     # except ValueError as error:
    #     #     self.show_message('Error', str(error))
    #     #     return None

    #     title = 'Sucesso'
    #     message = "Cliente cadastrado com sucesso!"
    #     QMessageBox.information(self.window, title, message)

    #     self.view.line_edit_nome_cliente.clear()
    #     self.view.line_edit_email_cliente.clear()
    #     self.view.line_edit_username_cliente.clear()
    #     self.view.line_edit_telefone_cliente.clear()
    #     self.view.line_edit_celular_cliente.clear()

    #     self.view.line_edit_logradouro_cliente.clear()
    #     self.view.line_edit_cidade_cliente.clear()
    #     self.view.line_edit_numero_cliente.clear()
    #     self.view.line_edit_bairro_cliente.clear()
    #     self.view.line_edit_cep_cliente.clear()
    #     self.view.line_edit_complemento_cliente.clear()


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
        UF = self.view.comboBoxUFZonaEntrega.currentText()
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
