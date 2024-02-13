# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 815)
        MainWindow.setMinimumSize(QSize(0, 815))
        self.actionAtualizar = QAction(MainWindow)
        self.actionAtualizar.setObjectName(u"actionAtualizar")
        self.actionCadastro = QAction(MainWindow)
        self.actionCadastro.setObjectName(u"actionCadastro")
        self.actionRemover = QAction(MainWindow)
        self.actionRemover.setObjectName(u"actionRemover")
        self.action_sair = QAction(MainWindow)
        self.action_sair.setObjectName(u"action_sair")
        self.action_historico = QAction(MainWindow)
        self.action_historico.setObjectName(u"action_historico")
        self.action_pedidos = QAction(MainWindow)
        self.action_pedidos.setObjectName(u"action_pedidos")
        self.actionDados_Cadastrais = QAction(MainWindow)
        self.actionDados_Cadastrais.setObjectName(u"actionDados_Cadastrais")
        self.actionCalculo_de_fracoes = QAction(MainWindow)
        self.actionCalculo_de_fracoes.setObjectName(u"actionCalculo_de_fracoes")
        self.action_calculo_de_fracoes = QAction(MainWindow)
        self.action_calculo_de_fracoes.setObjectName(u"action_calculo_de_fracoes")
        self.action_dados_cadastrais = QAction(MainWindow)
        self.action_dados_cadastrais.setObjectName(u"action_dados_cadastrais")
        self.action_categorias = QAction(MainWindow)
        self.action_categorias.setObjectName(u"action_categorias")
        self.action_precos_especiais = QAction(MainWindow)
        self.action_precos_especiais.setObjectName(u"action_precos_especiais")
        self.action_adicionais = QAction(MainWindow)
        self.action_adicionais.setObjectName(u"action_adicionais")
        self.action_combos = QAction(MainWindow)
        self.action_combos.setObjectName(u"action_combos")
        self.action_produtos = QAction(MainWindow)
        self.action_produtos.setObjectName(u"action_produtos")
        self.action_clientes = QAction(MainWindow)
        self.action_clientes.setObjectName(u"action_clientes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setMinimumSize(QSize(0, 35))
        self.tab_widget.setMaximumSize(QSize(16777215, 16777215))
        self.tab_status = QWidget()
        self.tab_status.setObjectName(u"tab_status")
        self.verticalLayout_13 = QVBoxLayout(self.tab_status)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.frame_34 = QFrame(self.tab_status)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_34)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout_15.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_nome_status_pedido = QLabel(self.frame_9)
        self.label_nome_status_pedido.setObjectName(u"label_nome_status_pedido")
        self.label_nome_status_pedido.setMaximumSize(QSize(16777215, 30))
        self.label_nome_status_pedido.setFont(font)

        self.verticalLayout_15.addWidget(self.label_nome_status_pedido, 0, Qt.AlignLeft)

        self.line_edit_nome_status_pedido = QLineEdit(self.frame_9)
        self.line_edit_nome_status_pedido.setObjectName(u"line_edit_nome_status_pedido")
        self.line_edit_nome_status_pedido.setMinimumSize(QSize(0, 35))

        self.verticalLayout_15.addWidget(self.line_edit_nome_status_pedido)

        self.label_descricao_status_pedido = QLabel(self.frame_9)
        self.label_descricao_status_pedido.setObjectName(u"label_descricao_status_pedido")
        self.label_descricao_status_pedido.setMaximumSize(QSize(16777215, 30))
        self.label_descricao_status_pedido.setFont(font)

        self.verticalLayout_15.addWidget(self.label_descricao_status_pedido, 0, Qt.AlignLeft)

        self.text_edit_descricao_status_pedido = QTextEdit(self.frame_9)
        self.text_edit_descricao_status_pedido.setObjectName(u"text_edit_descricao_status_pedido")
        self.text_edit_descricao_status_pedido.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_15.addWidget(self.text_edit_descricao_status_pedido)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_35)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(20, 20, 20, 20)
        self.label_status_cadastrados = QLabel(self.frame_35)
        self.label_status_cadastrados.setObjectName(u"label_status_cadastrados")
        self.label_status_cadastrados.setMaximumSize(QSize(16777215, 50))
        self.label_status_cadastrados.setFont(font)

        self.verticalLayout_27.addWidget(self.label_status_cadastrados, 0, Qt.AlignLeft)

        self.list_view_status_cadastrados = QListView(self.frame_35)
        self.list_view_status_cadastrados.setObjectName(u"list_view_status_cadastrados")
        self.list_view_status_cadastrados.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_27.addWidget(self.list_view_status_cadastrados)


        self.horizontalLayout_8.addWidget(self.frame_35)


        self.verticalLayout_13.addWidget(self.frame_34)

        self.frame_49 = QFrame(self.tab_status)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.push_button_cadastrar_status_pedido = QPushButton(self.frame_50)
        self.push_button_cadastrar_status_pedido.setObjectName(u"push_button_cadastrar_status_pedido")
        self.push_button_cadastrar_status_pedido.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_27.addWidget(self.push_button_cadastrar_status_pedido)


        self.horizontalLayout_28.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.push_button_remover_status = QPushButton(self.frame_51)
        self.push_button_remover_status.setObjectName(u"push_button_remover_status")
        self.push_button_remover_status.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_26.addWidget(self.push_button_remover_status)

        self.push_button_editar_status = QPushButton(self.frame_51)
        self.push_button_editar_status.setObjectName(u"push_button_editar_status")
        self.push_button_editar_status.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_26.addWidget(self.push_button_editar_status)


        self.horizontalLayout_28.addWidget(self.frame_51)


        self.verticalLayout_13.addWidget(self.frame_49)

        self.tab_widget.addTab(self.tab_status, "")
        self.tab_categoria = QWidget()
        self.tab_categoria.setObjectName(u"tab_categoria")
        self.verticalLayout_2 = QVBoxLayout(self.tab_categoria)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.frame_20 = QFrame(self.tab_categoria)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"#frame_20 {\n"
"    border: 0px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_20)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(False)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, 20, 20, 20)
        self.label_cadastrar_nova_categoria = QLabel(self.frame)
        self.label_cadastrar_nova_categoria.setObjectName(u"label_cadastrar_nova_categoria")
        self.label_cadastrar_nova_categoria.setMinimumSize(QSize(0, 100))
        self.label_cadastrar_nova_categoria.setMaximumSize(QSize(16777215, 100))
        self.label_cadastrar_nova_categoria.setFont(font)
        self.label_cadastrar_nova_categoria.setMouseTracking(False)

        self.verticalLayout_28.addWidget(self.label_cadastrar_nova_categoria, 0, Qt.AlignHCenter)

        self.label_nome_categoria_produto = QLabel(self.frame)
        self.label_nome_categoria_produto.setObjectName(u"label_nome_categoria_produto")
        self.label_nome_categoria_produto.setMaximumSize(QSize(16777215, 30))
        self.label_nome_categoria_produto.setFont(font)

        self.verticalLayout_28.addWidget(self.label_nome_categoria_produto, 0, Qt.AlignLeft)

        self.line_edit_nome_categoria_produto = QLineEdit(self.frame)
        self.line_edit_nome_categoria_produto.setObjectName(u"line_edit_nome_categoria_produto")
        self.line_edit_nome_categoria_produto.setMinimumSize(QSize(0, 35))

        self.verticalLayout_28.addWidget(self.line_edit_nome_categoria_produto)

        self.label_descricao_categoria_produto = QLabel(self.frame)
        self.label_descricao_categoria_produto.setObjectName(u"label_descricao_categoria_produto")
        self.label_descricao_categoria_produto.setMaximumSize(QSize(16777215, 30))
        self.label_descricao_categoria_produto.setFont(font)

        self.verticalLayout_28.addWidget(self.label_descricao_categoria_produto, 0, Qt.AlignLeft)

        self.text_edit_descricao_categoria_produto = QTextEdit(self.frame)
        self.text_edit_descricao_categoria_produto.setObjectName(u"text_edit_descricao_categoria_produto")
        self.text_edit_descricao_categoria_produto.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_28.addWidget(self.text_edit_descricao_categoria_produto)

        self.push_button_cadastrar_categoria_produto = QPushButton(self.frame)
        self.push_button_cadastrar_categoria_produto.setObjectName(u"push_button_cadastrar_categoria_produto")
        self.push_button_cadastrar_categoria_produto.setMinimumSize(QSize(0, 35))
        self.push_button_cadastrar_categoria_produto.setFont(font1)

        self.verticalLayout_28.addWidget(self.push_button_cadastrar_categoria_produto)


        self.horizontalLayout_13.addWidget(self.frame)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.label_categorias_cadastradas = QLabel(self.frame_21)
        self.label_categorias_cadastradas.setObjectName(u"label_categorias_cadastradas")
        self.label_categorias_cadastradas.setMaximumSize(QSize(16777215, 16777215))
        self.label_categorias_cadastradas.setFont(font)

        self.verticalLayout_11.addWidget(self.label_categorias_cadastradas, 0, Qt.AlignLeft)

        self.list_view_categorias_cadastradas = QListView(self.frame_21)
        self.list_view_categorias_cadastradas.setObjectName(u"list_view_categorias_cadastradas")
        self.list_view_categorias_cadastradas.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_11.addWidget(self.list_view_categorias_cadastradas)

        self.frame_54 = QFrame(self.frame_21)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy2)
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push_button_remover_categoria = QPushButton(self.frame_54)
        self.push_button_remover_categoria.setObjectName(u"push_button_remover_categoria")
        self.push_button_remover_categoria.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_4.addWidget(self.push_button_remover_categoria)

        self.push_button_editar_categoria = QPushButton(self.frame_54)
        self.push_button_editar_categoria.setObjectName(u"push_button_editar_categoria")
        self.push_button_editar_categoria.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_4.addWidget(self.push_button_editar_categoria)


        self.verticalLayout_11.addWidget(self.frame_54)


        self.horizontalLayout_13.addWidget(self.frame_21)


        self.verticalLayout_2.addWidget(self.frame_20)

        self.tab_widget.addTab(self.tab_categoria, "")
        self.tab_adicionais = QWidget()
        self.tab_adicionais.setObjectName(u"tab_adicionais")
        self.verticalLayout_5 = QVBoxLayout(self.tab_adicionais)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.frame_14 = QFrame(self.tab_adicionais)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14 {\n"
"    border: 0px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_14)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.label_novo_adicional = QLabel(self.frame_4)
        self.label_novo_adicional.setObjectName(u"label_novo_adicional")
        self.label_novo_adicional.setMinimumSize(QSize(0, 100))
        self.label_novo_adicional.setMaximumSize(QSize(16777215, 100))
        self.label_novo_adicional.setFont(font)

        self.verticalLayout_8.addWidget(self.label_novo_adicional, 0, Qt.AlignHCenter)

        self.label_nome_adicional = QLabel(self.frame_4)
        self.label_nome_adicional.setObjectName(u"label_nome_adicional")
        self.label_nome_adicional.setFont(font)

        self.verticalLayout_8.addWidget(self.label_nome_adicional)

        self.line_edit_nome_adicional = QLineEdit(self.frame_4)
        self.line_edit_nome_adicional.setObjectName(u"line_edit_nome_adicional")
        self.line_edit_nome_adicional.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.line_edit_nome_adicional)

        self.label_preco_adicional = QLabel(self.frame_4)
        self.label_preco_adicional.setObjectName(u"label_preco_adicional")
        self.label_preco_adicional.setFont(font)

        self.verticalLayout_8.addWidget(self.label_preco_adicional)

        self.double_spin_box_preco_adicional = QDoubleSpinBox(self.frame_4)
        self.double_spin_box_preco_adicional.setObjectName(u"double_spin_box_preco_adicional")
        self.double_spin_box_preco_adicional.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.double_spin_box_preco_adicional)

        self.label_descricao_adicional = QLabel(self.frame_4)
        self.label_descricao_adicional.setObjectName(u"label_descricao_adicional")
        self.label_descricao_adicional.setFont(font)

        self.verticalLayout_8.addWidget(self.label_descricao_adicional)

        self.text_edit_descricao_adicional = QTextEdit(self.frame_4)
        self.text_edit_descricao_adicional.setObjectName(u"text_edit_descricao_adicional")
        self.text_edit_descricao_adicional.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_8.addWidget(self.text_edit_descricao_adicional)

        self.push_button_cadastrar_adicional = QPushButton(self.frame_4)
        self.push_button_cadastrar_adicional.setObjectName(u"push_button_cadastrar_adicional")
        self.push_button_cadastrar_adicional.setMinimumSize(QSize(0, 35))
        self.push_button_cadastrar_adicional.setFont(font1)

        self.verticalLayout_8.addWidget(self.push_button_cadastrar_adicional)


        self.horizontalLayout_20.addWidget(self.frame_4)

        self.frame_23 = QFrame(self.frame_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(20, 20, 20, 20)
        self.label_adicionais_cadastrados = QLabel(self.frame_23)
        self.label_adicionais_cadastrados.setObjectName(u"label_adicionais_cadastrados")
        self.label_adicionais_cadastrados.setFont(font)

        self.verticalLayout_21.addWidget(self.label_adicionais_cadastrados)

        self.list_view_adicionais = QListView(self.frame_23)
        self.list_view_adicionais.setObjectName(u"list_view_adicionais")

        self.verticalLayout_21.addWidget(self.list_view_adicionais)

        self.push_button_remover_adicional = QPushButton(self.frame_23)
        self.push_button_remover_adicional.setObjectName(u"push_button_remover_adicional")
        self.push_button_remover_adicional.setMinimumSize(QSize(0, 35))

        self.verticalLayout_21.addWidget(self.push_button_remover_adicional)


        self.horizontalLayout_20.addWidget(self.frame_23)


        self.verticalLayout_5.addWidget(self.frame_14)

        self.tab_widget.addTab(self.tab_adicionais, "")
        self.tab_produto = QWidget()
        self.tab_produto.setObjectName(u"tab_produto")
        self.verticalLayout_7 = QVBoxLayout(self.tab_produto)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.label_novo_produto = QLabel(self.tab_produto)
        self.label_novo_produto.setObjectName(u"label_novo_produto")
        self.label_novo_produto.setMinimumSize(QSize(0, 100))
        self.label_novo_produto.setFont(font)

        self.verticalLayout_7.addWidget(self.label_novo_produto, 0, Qt.AlignHCenter)

        self.frame_37 = QFrame(self.tab_produto)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_48 = QFrame(self.frame_37)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_48)
        self.verticalLayout_35.setSpacing(8)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 8, 0, 0)
        self.label_6 = QLabel(self.frame_48)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_35.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.frame_47 = QFrame(self.frame_48)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_47)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_38)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_38)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_preco_produto = QLabel(self.frame_3)
        self.label_preco_produto.setObjectName(u"label_preco_produto")
        self.label_preco_produto.setFont(font)

        self.verticalLayout_4.addWidget(self.label_preco_produto)

        self.double_spin_box_preco_produto = QDoubleSpinBox(self.frame_3)
        self.double_spin_box_preco_produto.setObjectName(u"double_spin_box_preco_produto")
        self.double_spin_box_preco_produto.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.double_spin_box_preco_produto)

        self.label_nome_produto = QLabel(self.frame_3)
        self.label_nome_produto.setObjectName(u"label_nome_produto")
        self.label_nome_produto.setFont(font)

        self.verticalLayout_4.addWidget(self.label_nome_produto)

        self.line_edit_nome_produto = QLineEdit(self.frame_3)
        self.line_edit_nome_produto.setObjectName(u"line_edit_nome_produto")
        self.line_edit_nome_produto.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.line_edit_nome_produto)

        self.label_categoria_produto = QLabel(self.frame_3)
        self.label_categoria_produto.setObjectName(u"label_categoria_produto")
        self.label_categoria_produto.setFont(font)

        self.verticalLayout_4.addWidget(self.label_categoria_produto)

        self.combo_box_categoria_produto = QComboBox(self.frame_3)
        self.combo_box_categoria_produto.addItem("")
        self.combo_box_categoria_produto.setObjectName(u"combo_box_categoria_produto")
        self.combo_box_categoria_produto.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.combo_box_categoria_produto)

        self.label_descricao_produto = QLabel(self.frame_3)
        self.label_descricao_produto.setObjectName(u"label_descricao_produto")
        self.label_descricao_produto.setFont(font)

        self.verticalLayout_4.addWidget(self.label_descricao_produto)

        self.text_edit_descricao_produto = QTextEdit(self.frame_3)
        self.text_edit_descricao_produto.setObjectName(u"text_edit_descricao_produto")
        self.text_edit_descricao_produto.setMinimumSize(QSize(0, 100))

        self.verticalLayout_4.addWidget(self.text_edit_descricao_produto)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_29.addWidget(self.frame_6)

        self.frame_18 = QFrame(self.frame_38)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.push_button_escolher_imagem_produto = QPushButton(self.frame_18)
        self.push_button_escolher_imagem_produto.setObjectName(u"push_button_escolher_imagem_produto")
        self.push_button_escolher_imagem_produto.setMinimumSize(QSize(0, 40))
        self.push_button_escolher_imagem_produto.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.push_button_escolher_imagem_produto)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.label_arquivo_produto = QLabel(self.frame_19)
        self.label_arquivo_produto.setObjectName(u"label_arquivo_produto")
        self.label_arquivo_produto.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.label_arquivo_produto)

        self.label_produto_image_filename = QLabel(self.frame_19)
        self.label_produto_image_filename.setObjectName(u"label_produto_image_filename")

        self.horizontalLayout_6.addWidget(self.label_produto_image_filename)


        self.horizontalLayout_2.addWidget(self.frame_19)


        self.verticalLayout_29.addWidget(self.frame_18)


        self.horizontalLayout_25.addWidget(self.frame_38)

        self.frame_7 = QFrame(self.frame_47)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, 0)
        self.label_ingredientes = QLabel(self.frame_7)
        self.label_ingredientes.setObjectName(u"label_ingredientes")
        self.label_ingredientes.setFont(font)

        self.verticalLayout_10.addWidget(self.label_ingredientes, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"#frame_17 {  border: 0px;  }")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_nome_ingrediente = QLabel(self.frame_17)
        self.label_nome_ingrediente.setObjectName(u"label_nome_ingrediente")

        self.horizontalLayout_14.addWidget(self.label_nome_ingrediente)

        self.line_edit_nome_ingrediente = QLineEdit(self.frame_17)
        self.line_edit_nome_ingrediente.setObjectName(u"line_edit_nome_ingrediente")
        self.line_edit_nome_ingrediente.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_14.addWidget(self.line_edit_nome_ingrediente)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.label_descricao_ingredientes = QLabel(self.frame_7)
        self.label_descricao_ingredientes.setObjectName(u"label_descricao_ingredientes")
        self.label_descricao_ingredientes.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_descricao_ingredientes)

        self.text_edit_ingrediente_descricao = QTextEdit(self.frame_7)
        self.text_edit_ingrediente_descricao.setObjectName(u"text_edit_ingrediente_descricao")
        self.text_edit_ingrediente_descricao.setMinimumSize(QSize(0, 0))
        self.text_edit_ingrediente_descricao.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_10.addWidget(self.text_edit_ingrediente_descricao)

        self.frame_33 = QFrame(self.frame_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.push_button_adicionar_ingrediente = QPushButton(self.frame_33)
        self.push_button_adicionar_ingrediente.setObjectName(u"push_button_adicionar_ingrediente")
        self.push_button_adicionar_ingrediente.setMinimumSize(QSize(0, 35))
        self.push_button_adicionar_ingrediente.setFont(font1)

        self.horizontalLayout_15.addWidget(self.push_button_adicionar_ingrediente)

        self.push_button_remover_ingrediente = QPushButton(self.frame_33)
        self.push_button_remover_ingrediente.setObjectName(u"push_button_remover_ingrediente")
        self.push_button_remover_ingrediente.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_15.addWidget(self.push_button_remover_ingrediente)


        self.verticalLayout_10.addWidget(self.frame_33)

        self.list_view_ingredientes = QListView(self.frame_7)
        self.list_view_ingredientes.setObjectName(u"list_view_ingredientes")

        self.verticalLayout_10.addWidget(self.list_view_ingredientes)


        self.horizontalLayout_25.addWidget(self.frame_7)


        self.verticalLayout_35.addWidget(self.frame_47)


        self.horizontalLayout_11.addWidget(self.frame_48)

        self.frame_22 = QFrame(self.frame_37)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setSpacing(9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 6, 0, 0)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_19.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.list_view_produtos_cadastrados = QListView(self.frame_22)
        self.list_view_produtos_cadastrados.setObjectName(u"list_view_produtos_cadastrados")

        self.verticalLayout_19.addWidget(self.list_view_produtos_cadastrados)

        self.frame_32 = QFrame(self.frame_22)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_32)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.push_button_remover_produto = QPushButton(self.frame_32)
        self.push_button_remover_produto.setObjectName(u"push_button_remover_produto")
        self.push_button_remover_produto.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_7.addWidget(self.push_button_remover_produto)


        self.verticalLayout_19.addWidget(self.frame_32)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.verticalLayout_7.addWidget(self.frame_37)

        self.push_button_cadastrar_produto = QPushButton(self.tab_produto)
        self.push_button_cadastrar_produto.setObjectName(u"push_button_cadastrar_produto")
        self.push_button_cadastrar_produto.setMinimumSize(QSize(0, 40))
        self.push_button_cadastrar_produto.setFont(font)

        self.verticalLayout_7.addWidget(self.push_button_cadastrar_produto)

        self.tab_widget.addTab(self.tab_produto, "")
        self.tab_preco = QWidget()
        self.tab_preco.setObjectName(u"tab_preco")
        self.tab_preco.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.tab_preco)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.label_novo_preco = QLabel(self.tab_preco)
        self.label_novo_preco.setObjectName(u"label_novo_preco")
        self.label_novo_preco.setMinimumSize(QSize(0, 0))
        self.label_novo_preco.setMaximumSize(QSize(16777215, 100))
        self.label_novo_preco.setFont(font)

        self.verticalLayout_3.addWidget(self.label_novo_preco, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.tab_preco)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(15, 2, 15, 2)
        self.frame_25 = QFrame(self.frame_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"#frame_25 {\n"
"    border: 0px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"#frame_26 {\n"
"    border: 0px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 5, 0, 5)
        self.label = QLabel(self.frame_26)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_23.addWidget(self.label)

        self.combo_box_categorias_preco = QComboBox(self.frame_26)
        self.combo_box_categorias_preco.addItem("")
        self.combo_box_categorias_preco.setObjectName(u"combo_box_categorias_preco")
        self.combo_box_categorias_preco.setMinimumSize(QSize(0, 35))

        self.verticalLayout_23.addWidget(self.combo_box_categorias_preco)


        self.horizontalLayout_22.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"#frame_27 {\n"
"    border: 0px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_27)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 5, 0, 5)
        self.label_produto_preco = QLabel(self.frame_27)
        self.label_produto_preco.setObjectName(u"label_produto_preco")
        self.label_produto_preco.setFont(font)

        self.verticalLayout_24.addWidget(self.label_produto_preco)

        self.combo_box_produto_preco = QComboBox(self.frame_27)
        self.combo_box_produto_preco.addItem("")
        self.combo_box_produto_preco.setObjectName(u"combo_box_produto_preco")
        self.combo_box_produto_preco.setMinimumSize(QSize(0, 35))

        self.verticalLayout_24.addWidget(self.combo_box_produto_preco)


        self.horizontalLayout_22.addWidget(self.frame_27)


        self.verticalLayout_14.addWidget(self.frame_25)

        self.frame_28 = QFrame(self.frame_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_28 {\n"
"    border: 0px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"#frame_30 {\n"
"    border: 0px;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 5, 0, 5)
        self.label_dia_da_semana_preco = QLabel(self.frame_30)
        self.label_dia_da_semana_preco.setObjectName(u"label_dia_da_semana_preco")
        self.label_dia_da_semana_preco.setFont(font)

        self.verticalLayout_26.addWidget(self.label_dia_da_semana_preco)

        self.combo_box_dia_da_semana_preco = QComboBox(self.frame_30)
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.addItem("")
        self.combo_box_dia_da_semana_preco.setObjectName(u"combo_box_dia_da_semana_preco")
        self.combo_box_dia_da_semana_preco.setMinimumSize(QSize(0, 35))

        self.verticalLayout_26.addWidget(self.combo_box_dia_da_semana_preco)


        self.horizontalLayout_23.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"#frame_29 {\n"
"    border: 0px;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_29)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 5, 0, 5)
        self.label_valor_preco = QLabel(self.frame_29)
        self.label_valor_preco.setObjectName(u"label_valor_preco")
        self.label_valor_preco.setFont(font)

        self.verticalLayout_25.addWidget(self.label_valor_preco)

        self.double_spin_valor_preco = QDoubleSpinBox(self.frame_29)
        self.double_spin_valor_preco.setObjectName(u"double_spin_valor_preco")
        self.double_spin_valor_preco.setMinimumSize(QSize(0, 35))

        self.verticalLayout_25.addWidget(self.double_spin_valor_preco)


        self.horizontalLayout_23.addWidget(self.frame_29)


        self.verticalLayout_14.addWidget(self.frame_28)

        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, 0, -1)
        self.push_button_cadastrar_preco = QPushButton(self.frame_2)
        self.push_button_cadastrar_preco.setObjectName(u"push_button_cadastrar_preco")
        self.push_button_cadastrar_preco.setMinimumSize(QSize(0, 40))
        self.push_button_cadastrar_preco.setMaximumSize(QSize(16777215, 16777215))
        self.push_button_cadastrar_preco.setFont(font)

        self.verticalLayout_30.addWidget(self.push_button_cadastrar_preco)


        self.verticalLayout_14.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_24 = QFrame(self.tab_preco)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_24)
        self.verticalLayout_22.setSpacing(8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(20, 5, 20, 5)
        self.label_precos_cadastrados = QLabel(self.frame_24)
        self.label_precos_cadastrados.setObjectName(u"label_precos_cadastrados")
        self.label_precos_cadastrados.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label_precos_cadastrados.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_precos_cadastrados)

        self.list_view_precos_cadastrados = QListView(self.frame_24)
        self.list_view_precos_cadastrados.setObjectName(u"list_view_precos_cadastrados")

        self.verticalLayout_22.addWidget(self.list_view_precos_cadastrados)

        self.push_button_remover_preco = QPushButton(self.frame_24)
        self.push_button_remover_preco.setObjectName(u"push_button_remover_preco")
        self.push_button_remover_preco.setMinimumSize(QSize(0, 40))

        self.verticalLayout_22.addWidget(self.push_button_remover_preco)


        self.verticalLayout_3.addWidget(self.frame_24)

        self.tab_widget.addTab(self.tab_preco, "")
        self.tab_pedido = QWidget()
        self.tab_pedido.setObjectName(u"tab_pedido")
        self.verticalLayout_6 = QVBoxLayout(self.tab_pedido)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.tab_pedido)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 20, -1, -1)
        self.label_cadastrar_pedido = QLabel(self.frame_10)
        self.label_cadastrar_pedido.setObjectName(u"label_cadastrar_pedido")
        self.label_cadastrar_pedido.setMaximumSize(QSize(16777215, 60))
        self.label_cadastrar_pedido.setFont(font)

        self.verticalLayout_16.addWidget(self.label_cadastrar_pedido, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFocusPolicy(Qt.NoFocus)
        self.frame_11.setStyleSheet(u"#frame_11, #frame_12, #frame_5 {\n"
"  border: 0px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, -1, 2)
        self.scroll_area_column_1_pedido = QScrollArea(self.frame_11)
        self.scroll_area_column_1_pedido.setObjectName(u"scroll_area_column_1_pedido")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scroll_area_column_1_pedido.sizePolicy().hasHeightForWidth())
        self.scroll_area_column_1_pedido.setSizePolicy(sizePolicy3)
        self.scroll_area_column_1_pedido.setMinimumSize(QSize(0, 300))
        self.scroll_area_column_1_pedido.setStyleSheet(u"QLineEdit {\n"
"    padding-left: 5px;\n"
"}")
        self.scroll_area_column_1_pedido.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 320, 500))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_cliente_pedido = QLabel(self.scrollAreaWidgetContents_2)
        self.label_cliente_pedido.setObjectName(u"label_cliente_pedido")
        self.label_cliente_pedido.setFont(font)

        self.verticalLayout_20.addWidget(self.label_cliente_pedido)

        self.combo_box_cliente_pedido = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_box_cliente_pedido.addItem("")
        self.combo_box_cliente_pedido.setObjectName(u"combo_box_cliente_pedido")
        self.combo_box_cliente_pedido.setMinimumSize(QSize(0, 30))

        self.verticalLayout_20.addWidget(self.combo_box_cliente_pedido)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_3)

        self.label_contato_pedido = QLabel(self.scrollAreaWidgetContents_2)
        self.label_contato_pedido.setObjectName(u"label_contato_pedido")
        self.label_contato_pedido.setFont(font)

        self.verticalLayout_20.addWidget(self.label_contato_pedido)

        self.horizontal_layout_11 = QHBoxLayout()
        self.horizontal_layout_11.setObjectName(u"horizontal_layout_11")
        self.label_celular_pedido = QLabel(self.scrollAreaWidgetContents_2)
        self.label_celular_pedido.setObjectName(u"label_celular_pedido")
        self.label_celular_pedido.setMinimumSize(QSize(0, 30))
        self.label_celular_pedido.setFont(font1)

        self.horizontal_layout_11.addWidget(self.label_celular_pedido)

        self.line_edit_celular_pedido = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_celular_pedido.setObjectName(u"line_edit_celular_pedido")
        self.line_edit_celular_pedido.setMinimumSize(QSize(0, 30))
        self.line_edit_celular_pedido.setCursor(QCursor(Qt.IBeamCursor))
        self.line_edit_celular_pedido.setTabletTracking(False)

        self.horizontal_layout_11.addWidget(self.line_edit_celular_pedido)


        self.verticalLayout_20.addLayout(self.horizontal_layout_11)

        self.label_endereco_pedido = QLabel(self.scrollAreaWidgetContents_2)
        self.label_endereco_pedido.setObjectName(u"label_endereco_pedido")
        self.label_endereco_pedido.setFont(font)

        self.verticalLayout_20.addWidget(self.label_endereco_pedido)

        self.horizontal_layout_4 = QHBoxLayout()
        self.horizontal_layout_4.setObjectName(u"horizontal_layout_4")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontal_layout_4.addWidget(self.label_7)

        self.line_edit_cep = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_cep.setObjectName(u"line_edit_cep")
        self.line_edit_cep.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_4.addWidget(self.line_edit_cep)

        self.combo_box_uf_pedido = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_box_uf_pedido.addItem("")
        self.combo_box_uf_pedido.addItem("")
        self.combo_box_uf_pedido.addItem("")
        self.combo_box_uf_pedido.setObjectName(u"combo_box_uf_pedido")
        self.combo_box_uf_pedido.setMinimumSize(QSize(80, 35))

        self.horizontal_layout_4.addWidget(self.combo_box_uf_pedido)


        self.verticalLayout_20.addLayout(self.horizontal_layout_4)

        self.line_edit_logradouro_pedido = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_logradouro_pedido.setObjectName(u"line_edit_logradouro_pedido")
        self.line_edit_logradouro_pedido.setMinimumSize(QSize(0, 30))

        self.verticalLayout_20.addWidget(self.line_edit_logradouro_pedido)

        self.horizontal_layout_8 = QHBoxLayout()
        self.horizontal_layout_8.setObjectName(u"horizontal_layout_8")
        self.line_edit_numero_end = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_numero_end.setObjectName(u"line_edit_numero_end")
        self.line_edit_numero_end.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_8.addWidget(self.line_edit_numero_end)

        self.line_edit_complemento = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_complemento.setObjectName(u"line_edit_complemento")
        self.line_edit_complemento.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_8.addWidget(self.line_edit_complemento)


        self.verticalLayout_20.addLayout(self.horizontal_layout_8)

        self.horizontal_layout_9 = QHBoxLayout()
        self.horizontal_layout_9.setObjectName(u"horizontal_layout_9")
        self.line_edit_bairro = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_bairro.setObjectName(u"line_edit_bairro")
        self.line_edit_bairro.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_9.addWidget(self.line_edit_bairro)

        self.line_edit_cidade = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_cidade.setObjectName(u"line_edit_cidade")
        self.line_edit_cidade.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_9.addWidget(self.line_edit_cidade)


        self.verticalLayout_20.addLayout(self.horizontal_layout_9)

        self.horizontal_layout_10 = QHBoxLayout()
        self.horizontal_layout_10.setObjectName(u"horizontal_layout_10")
        self.label_frete_pedido = QLabel(self.scrollAreaWidgetContents_2)
        self.label_frete_pedido.setObjectName(u"label_frete_pedido")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_frete_pedido.setFont(font3)

        self.horizontal_layout_10.addWidget(self.label_frete_pedido)

        self.double_spin_box_frete_pedido = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.double_spin_box_frete_pedido.setObjectName(u"double_spin_box_frete_pedido")
        self.double_spin_box_frete_pedido.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_10.addWidget(self.double_spin_box_frete_pedido)


        self.verticalLayout_20.addLayout(self.horizontal_layout_10)

        self.scroll_area_column_1_pedido.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scroll_area_column_1_pedido)

        self.scroll_area_column_2_pedido = QScrollArea(self.frame_11)
        self.scroll_area_column_2_pedido.setObjectName(u"scroll_area_column_2_pedido")
        sizePolicy3.setHeightForWidth(self.scroll_area_column_2_pedido.sizePolicy().hasHeightForWidth())
        self.scroll_area_column_2_pedido.setSizePolicy(sizePolicy3)
        self.scroll_area_column_2_pedido.setMinimumSize(QSize(300, 0))
        self.scroll_area_column_2_pedido.setFrameShape(QFrame.StyledPanel)
        self.scroll_area_column_2_pedido.setWidgetResizable(True)
        self.scroll_area_widget_contents_2 = QWidget()
        self.scroll_area_widget_contents_2.setObjectName(u"scroll_area_widget_contents_2")
        self.scroll_area_widget_contents_2.setGeometry(QRect(0, 0, 284, 713))
        self.verticalLayout_9 = QVBoxLayout(self.scroll_area_widget_contents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_13 = QFrame(self.scroll_area_widget_contents_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_13)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.label_item_pedido = QLabel(self.frame_13)
        self.label_item_pedido.setObjectName(u"label_item_pedido")
        self.label_item_pedido.setFont(font)

        self.verticalLayout_31.addWidget(self.label_item_pedido)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.label_4)

        self.combo_box_categoria_pedido = QComboBox(self.frame_13)
        self.combo_box_categoria_pedido.addItem("")
        self.combo_box_categoria_pedido.setObjectName(u"combo_box_categoria_pedido")
        self.combo_box_categoria_pedido.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.combo_box_categoria_pedido)


        self.verticalLayout_31.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.label_3)

        self.combo_box_item_pedido = QComboBox(self.frame_13)
        self.combo_box_item_pedido.addItem("")
        self.combo_box_item_pedido.addItem("")
        self.combo_box_item_pedido.addItem("")
        self.combo_box_item_pedido.setObjectName(u"combo_box_item_pedido")
        self.combo_box_item_pedido.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.combo_box_item_pedido)


        self.verticalLayout_31.addLayout(self.horizontalLayout_10)

        self.horizontal_layout_7 = QHBoxLayout()
        self.horizontal_layout_7.setObjectName(u"horizontal_layout_7")
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_7.addWidget(self.label_2)

        self.spin_box_item_pedido = QSpinBox(self.frame_13)
        self.spin_box_item_pedido.setObjectName(u"spin_box_item_pedido")
        self.spin_box_item_pedido.setMinimumSize(QSize(0, 30))
        self.spin_box_item_pedido.setAccelerated(False)
        self.spin_box_item_pedido.setMinimum(1)

        self.horizontal_layout_7.addWidget(self.spin_box_item_pedido)


        self.verticalLayout_31.addLayout(self.horizontal_layout_7)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_44 = QFrame(self.scroll_area_widget_contents_2)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_44)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, -1, 0, -1)
        self.label_adicionais_pedido = QLabel(self.frame_44)
        self.label_adicionais_pedido.setObjectName(u"label_adicionais_pedido")
        self.label_adicionais_pedido.setFont(font)

        self.verticalLayout_32.addWidget(self.label_adicionais_pedido)

        self.horizontal_layout_15 = QHBoxLayout()
        self.horizontal_layout_15.setObjectName(u"horizontal_layout_15")
        self.combo_box_adicional_pedido = QComboBox(self.frame_44)
        self.combo_box_adicional_pedido.addItem("")
        self.combo_box_adicional_pedido.addItem("")
        self.combo_box_adicional_pedido.setObjectName(u"combo_box_adicional_pedido")
        self.combo_box_adicional_pedido.setMinimumSize(QSize(120, 30))

        self.horizontal_layout_15.addWidget(self.combo_box_adicional_pedido)

        self.spin_box_quantidade_acicionais = QSpinBox(self.frame_44)
        self.spin_box_quantidade_acicionais.setObjectName(u"spin_box_quantidade_acicionais")
        self.spin_box_quantidade_acicionais.setMinimumSize(QSize(0, 30))

        self.horizontal_layout_15.addWidget(self.spin_box_quantidade_acicionais)

        self.push_button_plus_adicional_pedido = QPushButton(self.frame_44)
        self.push_button_plus_adicional_pedido.setObjectName(u"push_button_plus_adicional_pedido")
        self.push_button_plus_adicional_pedido.setMinimumSize(QSize(30, 30))
        self.push_button_plus_adicional_pedido.setMaximumSize(QSize(16777215, 16777215))
        self.push_button_plus_adicional_pedido.setFont(font)

        self.horizontal_layout_15.addWidget(self.push_button_plus_adicional_pedido)


        self.verticalLayout_32.addLayout(self.horizontal_layout_15)

        self.list_widget_adicionais_pedido = QListWidget(self.frame_44)
        self.list_widget_adicionais_pedido.setObjectName(u"list_widget_adicionais_pedido")
        self.list_widget_adicionais_pedido.setMinimumSize(QSize(0, 120))
        self.list_widget_adicionais_pedido.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_32.addWidget(self.list_widget_adicionais_pedido)


        self.verticalLayout_9.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.scroll_area_widget_contents_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_45)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.label_ingredientes_pedido = QLabel(self.frame_45)
        self.label_ingredientes_pedido.setObjectName(u"label_ingredientes_pedido")
        self.label_ingredientes_pedido.setFont(font)

        self.verticalLayout_33.addWidget(self.label_ingredientes_pedido)

        self.scroll_area_ingredientes = QScrollArea(self.frame_45)
        self.scroll_area_ingredientes.setObjectName(u"scroll_area_ingredientes")
        self.scroll_area_ingredientes.setMinimumSize(QSize(0, 120))
        self.scroll_area_ingredientes.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 264, 118))
        self.scroll_area_ingredientes.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_33.addWidget(self.scroll_area_ingredientes)


        self.verticalLayout_9.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.scroll_area_widget_contents_2)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_46)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, -1, 0, -1)
        self.label_observacoes_pedido = QLabel(self.frame_46)
        self.label_observacoes_pedido.setObjectName(u"label_observacoes_pedido")
        self.label_observacoes_pedido.setFont(font)

        self.verticalLayout_34.addWidget(self.label_observacoes_pedido)

        self.text_edit_observacao_item = QTextEdit(self.frame_46)
        self.text_edit_observacao_item.setObjectName(u"text_edit_observacao_item")
        self.text_edit_observacao_item.setMinimumSize(QSize(0, 60))
        self.text_edit_observacao_item.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_34.addWidget(self.text_edit_observacao_item)


        self.verticalLayout_9.addWidget(self.frame_46)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.push_button_adicionar_item_pedido = QPushButton(self.scroll_area_widget_contents_2)
        self.push_button_adicionar_item_pedido.setObjectName(u"push_button_adicionar_item_pedido")
        self.push_button_adicionar_item_pedido.setMinimumSize(QSize(0, 35))

        self.verticalLayout_9.addWidget(self.push_button_adicionar_item_pedido)

        self.scroll_area_column_2_pedido.setWidget(self.scroll_area_widget_contents_2)

        self.horizontalLayout.addWidget(self.scroll_area_column_2_pedido)

        self.frame_column_3_pedido = QFrame(self.frame_11)
        self.frame_column_3_pedido.setObjectName(u"frame_column_3_pedido")
        self.frame_column_3_pedido.setFocusPolicy(Qt.NoFocus)
        self.frame_column_3_pedido.setStyleSheet(u"#frame_13 {  border: 0px;  }")
        self.frame_column_3_pedido.setFrameShape(QFrame.StyledPanel)
        self.frame_column_3_pedido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_column_3_pedido)
        self.verticalLayout_18.setSpacing(9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, 9, -1, 9)
        self.label_image_produto_text = QLabel(self.frame_column_3_pedido)
        self.label_image_produto_text.setObjectName(u"label_image_produto_text")
        self.label_image_produto_text.setFont(font)

        self.verticalLayout_18.addWidget(self.label_image_produto_text)

        self.frame_31 = QFrame(self.frame_column_3_pedido)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy1)
        self.frame_31.setMinimumSize(QSize(0, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_31)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_image = QLabel(self.frame_31)
        self.label_image.setObjectName(u"label_image")

        self.verticalLayout_36.addWidget(self.label_image)


        self.verticalLayout_18.addWidget(self.frame_31)

        self.label_13 = QLabel(self.frame_column_3_pedido)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_18.addWidget(self.label_13)

        self.table_widget_item_pedido = QTableWidget(self.frame_column_3_pedido)
        if (self.table_widget_item_pedido.columnCount() < 6):
            self.table_widget_item_pedido.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_widget_item_pedido.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_widget_item_pedido.setObjectName(u"table_widget_item_pedido")

        self.verticalLayout_18.addWidget(self.table_widget_item_pedido)

        self.frame_16 = QFrame(self.frame_column_3_pedido)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 45))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_total_item_pedido = QLabel(self.frame_16)
        self.label_total_item_pedido.setObjectName(u"label_total_item_pedido")
        self.label_total_item_pedido.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label_total_item_pedido)

        self.line_edit_total_item_pedido = QLineEdit(self.frame_16)
        self.line_edit_total_item_pedido.setObjectName(u"line_edit_total_item_pedido")
        self.line_edit_total_item_pedido.setEnabled(False)
        self.line_edit_total_item_pedido.setMaximumSize(QSize(100, 16777215))
        self.line_edit_total_item_pedido.setStyleSheet(u"border: 0px;")

        self.horizontalLayout_3.addWidget(self.line_edit_total_item_pedido)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.horizontalLayout.addWidget(self.frame_column_3_pedido)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.line_4 = QFrame(self.frame_10)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_4)

        self.label_comentarios_pedido = QLabel(self.frame_10)
        self.label_comentarios_pedido.setObjectName(u"label_comentarios_pedido")
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.label_comentarios_pedido.setFont(font4)

        self.verticalLayout_16.addWidget(self.label_comentarios_pedido)

        self.text_edit_comentarios_pedido = QTextEdit(self.frame_10)
        self.text_edit_comentarios_pedido.setObjectName(u"text_edit_comentarios_pedido")
        self.text_edit_comentarios_pedido.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_16.addWidget(self.text_edit_comentarios_pedido)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.push_button_cadastrar_pedido = QPushButton(self.tab_pedido)
        self.push_button_cadastrar_pedido.setObjectName(u"push_button_cadastrar_pedido")
        self.push_button_cadastrar_pedido.setMinimumSize(QSize(0, 40))
        self.push_button_cadastrar_pedido.setFont(font)

        self.verticalLayout_6.addWidget(self.push_button_cadastrar_pedido)

        self.tab_widget.addTab(self.tab_pedido, "")
        self.tab_combos = QWidget()
        self.tab_combos.setObjectName(u"tab_combos")
        self.tab_widget.addTab(self.tab_combos, "")
        self.tab_cliente = QWidget()
        self.tab_cliente.setObjectName(u"tab_cliente")
        self.gridLayout = QGridLayout(self.tab_cliente)
        self.gridLayout.setObjectName(u"gridLayout")
        self.push_button_cadastrar_cliente = QPushButton(self.tab_cliente)
        self.push_button_cadastrar_cliente.setObjectName(u"push_button_cadastrar_cliente")
        self.push_button_cadastrar_cliente.setMinimumSize(QSize(0, 40))
        self.push_button_cadastrar_cliente.setFont(font)

        self.gridLayout.addWidget(self.push_button_cadastrar_cliente, 7, 0, 1, 1)

        self.frame_15 = QFrame(self.tab_cliente)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.frame_41 = QFrame(self.frame_15)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.line_edit_nome_cliente = QLineEdit(self.frame_41)
        self.line_edit_nome_cliente.setObjectName(u"line_edit_nome_cliente")
        self.line_edit_nome_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_nome_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.line_edit_nome_cliente)


        self.verticalLayout_17.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_15)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.line_edit_email_cliente = QLineEdit(self.frame_42)
        self.line_edit_email_cliente.setObjectName(u"line_edit_email_cliente")
        self.line_edit_email_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_email_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.line_edit_email_cliente)

        self.line_edit_username_cliente = QLineEdit(self.frame_42)
        self.line_edit_username_cliente.setObjectName(u"line_edit_username_cliente")
        self.line_edit_username_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_username_cliente.setMaximumSize(QSize(16777215, 16777215))
        self.line_edit_username_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.line_edit_username_cliente)


        self.verticalLayout_17.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_15)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.line_edit_celular_cliente = QLineEdit(self.frame_43)
        self.line_edit_celular_cliente.setObjectName(u"line_edit_celular_cliente")
        self.line_edit_celular_cliente.setMinimumSize(QSize(200, 35))
        self.line_edit_celular_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.line_edit_celular_cliente)

        self.line_edit_telefone_cliente = QLineEdit(self.frame_43)
        self.line_edit_telefone_cliente.setObjectName(u"line_edit_telefone_cliente")
        self.line_edit_telefone_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_telefone_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.line_edit_telefone_cliente)


        self.verticalLayout_17.addWidget(self.frame_43)


        self.gridLayout.addWidget(self.frame_15, 2, 0, 1, 1)

        self.label_cadastro_cliente = QLabel(self.tab_cliente)
        self.label_cadastro_cliente.setObjectName(u"label_cadastro_cliente")
        self.label_cadastro_cliente.setMinimumSize(QSize(0, 100))
        self.label_cadastro_cliente.setMaximumSize(QSize(16777215, 100))
        self.label_cadastro_cliente.setFont(font)
        self.label_cadastro_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_cadastro_cliente, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.tab_cliente)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.frame_40 = QFrame(self.frame_5)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.line_edit_cep_cliente = QLineEdit(self.frame_40)
        self.line_edit_cep_cliente.setObjectName(u"line_edit_cep_cliente")
        self.line_edit_cep_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_cep_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.line_edit_cep_cliente)

        self.line_edit_cidade_cliente = QLineEdit(self.frame_40)
        self.line_edit_cidade_cliente.setObjectName(u"line_edit_cidade_cliente")
        self.line_edit_cidade_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_cidade_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.line_edit_cidade_cliente)

        self.combo_box_uf_cliente = QComboBox(self.frame_40)
        self.combo_box_uf_cliente.setObjectName(u"combo_box_uf_cliente")
        self.combo_box_uf_cliente.setMinimumSize(QSize(0, 35))
        self.combo_box_uf_cliente.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_18.addWidget(self.combo_box_uf_cliente)


        self.verticalLayout_12.addWidget(self.frame_40)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.line_edit_logradouro_cliente = QLineEdit(self.frame_12)
        self.line_edit_logradouro_cliente.setObjectName(u"line_edit_logradouro_cliente")
        self.line_edit_logradouro_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_logradouro_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.line_edit_logradouro_cliente)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_39 = QFrame(self.frame_5)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.line_edit_numero_cliente = QLineEdit(self.frame_39)
        self.line_edit_numero_cliente.setObjectName(u"line_edit_numero_cliente")
        self.line_edit_numero_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_numero_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.line_edit_numero_cliente)

        self.line_edit_complemento_cliente = QLineEdit(self.frame_39)
        self.line_edit_complemento_cliente.setObjectName(u"line_edit_complemento_cliente")
        self.line_edit_complemento_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_complemento_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.line_edit_complemento_cliente)

        self.line_edit_bairro_cliente = QLineEdit(self.frame_39)
        self.line_edit_bairro_cliente.setObjectName(u"line_edit_bairro_cliente")
        self.line_edit_bairro_cliente.setMinimumSize(QSize(0, 35))
        self.line_edit_bairro_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.line_edit_bairro_cliente)


        self.verticalLayout_12.addWidget(self.frame_39)


        self.gridLayout.addWidget(self.frame_5, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(50, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.label_dados_cliente = QLabel(self.tab_cliente)
        self.label_dados_cliente.setObjectName(u"label_dados_cliente")
        self.label_dados_cliente.setMinimumSize(QSize(0, 40))
        self.label_dados_cliente.setMaximumSize(QSize(16777215, 100))
        self.label_dados_cliente.setFont(font)
        self.label_dados_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_dados_cliente, 1, 0, 1, 1)

        self.label_endereco_cliente = QLabel(self.tab_cliente)
        self.label_endereco_cliente.setObjectName(u"label_endereco_cliente")
        self.label_endereco_cliente.setMinimumSize(QSize(0, 40))
        self.label_endereco_cliente.setMaximumSize(QSize(16777215, 100))
        self.label_endereco_cliente.setBaseSize(QSize(0, 0))
        self.label_endereco_cliente.setFont(font)
        self.label_endereco_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_endereco_cliente, 4, 0, 1, 1)

        self.tab_widget.addTab(self.tab_cliente, "")

        self.verticalLayout.addWidget(self.tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 919, 22))
        self.menu_arquivo = QMenu(self.menubar)
        self.menu_arquivo.setObjectName(u"menu_arquivo")
        self.menu_sobre = QMenu(self.menubar)
        self.menu_sobre.setObjectName(u"menu_sobre")
        self.menu_exibir = QMenu(self.menubar)
        self.menu_exibir.setObjectName(u"menu_exibir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_arquivo.menuAction())
        self.menubar.addAction(self.menu_sobre.menuAction())
        self.menubar.addAction(self.menu_exibir.menuAction())
        self.menu_arquivo.addAction(self.action_sair)
        self.menu_sobre.addAction(self.action_dados_cadastrais)
        self.menu_sobre.addAction(self.action_calculo_de_fracoes)
        self.menu_exibir.addAction(self.action_historico)
        self.menu_exibir.addAction(self.action_pedidos)
        self.menu_exibir.addAction(self.action_categorias)
        self.menu_exibir.addAction(self.action_precos_especiais)
        self.menu_exibir.addAction(self.action_adicionais)
        self.menu_exibir.addAction(self.action_combos)
        self.menu_exibir.addAction(self.action_produtos)
        self.menu_exibir.addAction(self.action_clientes)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chickie", None))
        self.actionAtualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.actionCadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.actionRemover.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.action_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.action_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.action_pedidos.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.actionDados_Cadastrais.setText(QCoreApplication.translate("MainWindow", u"Dados Cadastrais", None))
        self.actionCalculo_de_fracoes.setText(QCoreApplication.translate("MainWindow", u"Calculo de fracoes", None))
        self.action_calculo_de_fracoes.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo de C\u00e1lculo de fra\u00e7\u00f5es", None))
        self.action_dados_cadastrais.setText(QCoreApplication.translate("MainWindow", u"Dados cadastrais", None))
        self.action_categorias.setText(QCoreApplication.translate("MainWindow", u"Categorias", None))
        self.action_precos_especiais.setText(QCoreApplication.translate("MainWindow", u"Precos especiais", None))
        self.action_adicionais.setText(QCoreApplication.translate("MainWindow", u"Adicionais", None))
        self.action_combos.setText(QCoreApplication.translate("MainWindow", u"Combos", None))
        self.action_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.action_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cadastrar novo status", None))
        self.label_nome_status_pedido.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_descricao_status_pedido.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_status_cadastrados.setText(QCoreApplication.translate("MainWindow", u"Status cadastrados", None))
        self.push_button_cadastrar_status_pedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar status", None))
        self.push_button_remover_status.setText(QCoreApplication.translate("MainWindow", u"Remover Status", None))
        self.push_button_editar_status.setText(QCoreApplication.translate("MainWindow", u"Editar Status", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_status), QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_cadastrar_nova_categoria.setText(QCoreApplication.translate("MainWindow", u"Cadastrar nova categoria", None))
        self.label_nome_categoria_produto.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.line_edit_nome_categoria_produto.setText("")
        self.label_descricao_categoria_produto.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.push_button_cadastrar_categoria_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar categoria", None))
        self.label_categorias_cadastradas.setText(QCoreApplication.translate("MainWindow", u"Categorias cadastradas", None))
        self.push_button_remover_categoria.setText(QCoreApplication.translate("MainWindow", u"Remover categoria", None))
        self.push_button_editar_categoria.setText(QCoreApplication.translate("MainWindow", u"Editar categoria", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_categoria), QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label_novo_adicional.setText(QCoreApplication.translate("MainWindow", u"Cadastrar adicional", None))
        self.label_nome_adicional.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_preco_adicional.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.label_descricao_adicional.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.push_button_cadastrar_adicional.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_adicionais_cadastrados.setText(QCoreApplication.translate("MainWindow", u"Adicionais cadastrados", None))
        self.push_button_remover_adicional.setText(QCoreApplication.translate("MainWindow", u"Remover Adicional", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_adicionais), QCoreApplication.translate("MainWindow", u"Adicionais", None))
        self.label_novo_produto.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cadastar Produto", None))
        self.label_preco_produto.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o base", None))
        self.label_nome_produto.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.line_edit_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_categoria_produto.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.combo_box_categoria_produto.setItemText(0, QCoreApplication.translate("MainWindow", u"Categoria A", None))

        self.label_descricao_produto.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.text_edit_descricao_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.push_button_escolher_imagem_produto.setText(QCoreApplication.translate("MainWindow", u"Escolher imagem", None))
        self.label_arquivo_produto.setText(QCoreApplication.translate("MainWindow", u"Arquivo:", None))
        self.label_produto_image_filename.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_ingredientes.setText(QCoreApplication.translate("MainWindow", u"Ingredientes", None))
        self.label_nome_ingrediente.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_descricao_ingredientes.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.push_button_adicionar_ingrediente.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.push_button_remover_ingrediente.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Produtos Cadastrados", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Editar produto", None))
        self.push_button_remover_produto.setText(QCoreApplication.translate("MainWindow", u"Remover produto", None))
        self.push_button_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_produto), QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_novo_preco.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7os", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.combo_box_categorias_preco.setItemText(0, QCoreApplication.translate("MainWindow", u"Pizzas", None))

        self.label_produto_preco.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.combo_box_produto_preco.setItemText(0, QCoreApplication.translate("MainWindow", u"Pizza tal", None))

        self.label_dia_da_semana_preco.setText(QCoreApplication.translate("MainWindow", u"Dia da semana", None))
        self.combo_box_dia_da_semana_preco.setItemText(0, QCoreApplication.translate("MainWindow", u"Segunda", None))
        self.combo_box_dia_da_semana_preco.setItemText(1, QCoreApplication.translate("MainWindow", u"Ter\u00e7a", None))
        self.combo_box_dia_da_semana_preco.setItemText(2, QCoreApplication.translate("MainWindow", u"Quarta", None))
        self.combo_box_dia_da_semana_preco.setItemText(3, QCoreApplication.translate("MainWindow", u"Quinta", None))
        self.combo_box_dia_da_semana_preco.setItemText(4, QCoreApplication.translate("MainWindow", u"Sexta", None))
        self.combo_box_dia_da_semana_preco.setItemText(5, QCoreApplication.translate("MainWindow", u"S\u00e1bado", None))
        self.combo_box_dia_da_semana_preco.setItemText(6, QCoreApplication.translate("MainWindow", u"Domingo", None))

        self.label_valor_preco.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.push_button_cadastrar_preco.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_precos_cadastrados.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7os cadastrados", None))
        self.push_button_remover_preco.setText(QCoreApplication.translate("MainWindow", u"Remover preco", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_preco), QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.label_cadastrar_pedido.setText(QCoreApplication.translate("MainWindow", u"Novo Pedido", None))
        self.label_cliente_pedido.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.combo_box_cliente_pedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha um cliente...", None))

        self.label_contato_pedido.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label_celular_pedido.setText(QCoreApplication.translate("MainWindow", u"Celular   ", None))
        self.line_edit_celular_pedido.setInputMask(QCoreApplication.translate("MainWindow", u"(00) 0 0000-0000", None))
        self.line_edit_celular_pedido.setText(QCoreApplication.translate("MainWindow", u"(00) 0 0000-0000", None))
        self.line_edit_celular_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular (00) 0 0000-0000", None))
        self.label_endereco_pedido.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.line_edit_cep.setInputMask(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.line_edit_cep.setText(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.line_edit_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.combo_box_uf_pedido.setItemText(0, QCoreApplication.translate("MainWindow", u"RJ", None))
        self.combo_box_uf_pedido.setItemText(1, QCoreApplication.translate("MainWindow", u"SP", None))
        self.combo_box_uf_pedido.setItemText(2, QCoreApplication.translate("MainWindow", u"SC", None))

        self.line_edit_logradouro_pedido.setText("")
        self.line_edit_logradouro_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.line_edit_numero_end.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.line_edit_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.line_edit_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.line_edit_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_frete_pedido.setText(QCoreApplication.translate("MainWindow", u"Frete", None))
        self.label_item_pedido.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.combo_box_categoria_pedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Pizzas", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.combo_box_item_pedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha ...", None))
        self.combo_box_item_pedido.setItemText(1, QCoreApplication.translate("MainWindow", u"Pizza fulana", None))
        self.combo_box_item_pedido.setItemText(2, QCoreApplication.translate("MainWindow", u"Pizza beutrana", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_adicionais_pedido.setText(QCoreApplication.translate("MainWindow", u"Adicionais", None))
        self.combo_box_adicional_pedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Muzzarela", None))
        self.combo_box_adicional_pedido.setItemText(1, QCoreApplication.translate("MainWindow", u"Champignon", None))

        self.push_button_plus_adicional_pedido.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_ingredientes_pedido.setText(QCoreApplication.translate("MainWindow", u"Ingredientes", None))
        self.label_observacoes_pedido.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.text_edit_observacao_item.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.push_button_adicionar_item_pedido.setText(QCoreApplication.translate("MainWindow", u"Adicionar Item", None))
        self.label_image_produto_text.setText(QCoreApplication.translate("MainWindow", u"Imagem do produto", None))
        self.label_image.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Itens", None))
        ___qtablewidgetitem = self.table_widget_item_pedido.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem1 = self.table_widget_item_pedido.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem2 = self.table_widget_item_pedido.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem3 = self.table_widget_item_pedido.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None));
        ___qtablewidgetitem4 = self.table_widget_item_pedido.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        ___qtablewidgetitem5 = self.table_widget_item_pedido.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ingredientes", None));
        self.label_total_item_pedido.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Total:</span></p></body></html>", None))
        self.line_edit_total_item_pedido.setText("")
        self.label_comentarios_pedido.setText(QCoreApplication.translate("MainWindow", u"Coment\u00e1rios do pedido", None))
        self.push_button_cadastrar_pedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_pedido), QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_combos), QCoreApplication.translate("MainWindow", u"Combos", None))
        self.push_button_cadastrar_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.line_edit_nome_cliente.setText("")
        self.line_edit_nome_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.line_edit_email_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.line_edit_username_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.line_edit_celular_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.line_edit_telefone_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_cadastro_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastro de cliente", None))
        self.line_edit_cep_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.line_edit_cidade_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.line_edit_logradouro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.line_edit_numero_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.line_edit_complemento_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.line_edit_bairro_cliente.setText("")
        self.line_edit_bairro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_dados_cliente.setText(QCoreApplication.translate("MainWindow", u"Dados Pessoais", None))
        self.label_endereco_cliente.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_cliente), QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.menu_arquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menu_sobre.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menu_exibir.setTitle(QCoreApplication.translate("MainWindow", u"Exibir", None))
    # retranslateUi

