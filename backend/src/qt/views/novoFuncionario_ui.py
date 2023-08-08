# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novoFuncionario.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_Chickie(object):
    def setupUi(self, Chickie):
        if not Chickie.objectName():
            Chickie.setObjectName(u"Chickie")
        Chickie.resize(800, 600)
        self.actionCategoria = QAction(Chickie)
        self.actionCategoria.setObjectName(u"actionCategoria")
        self.actionNovaCategoria = QAction(Chickie)
        self.actionNovaCategoria.setObjectName(u"actionNovaCategoria")
        self.actionNovoEntregador = QAction(Chickie)
        self.actionNovoEntregador.setObjectName(u"actionNovoEntregador")
        self.actionFeedback = QAction(Chickie)
        self.actionFeedback.setObjectName(u"actionFeedback")
        self.actionNovoFuncionario = QAction(Chickie)
        self.actionNovoFuncionario.setObjectName(u"actionNovoFuncionario")
        self.actionNovoMetodoDePagamento = QAction(Chickie)
        self.actionNovoMetodoDePagamento.setObjectName(u"actionNovoMetodoDePagamento")
        self.actionNovaZonaDeEntrega = QAction(Chickie)
        self.actionNovaZonaDeEntrega.setObjectName(u"actionNovaZonaDeEntrega")
        self.actionNovoCliente = QAction(Chickie)
        self.actionNovoCliente.setObjectName(u"actionNovoCliente")
        self.actionPedido = QAction(Chickie)
        self.actionPedido.setObjectName(u"actionPedido")
        self.actionNovoPreco = QAction(Chickie)
        self.actionNovoPreco.setObjectName(u"actionNovoPreco")
        self.actionNovoPedido = QAction(Chickie)
        self.actionNovoPedido.setObjectName(u"actionNovoPedido")
        self.actionPreco_2 = QAction(Chickie)
        self.actionPreco_2.setObjectName(u"actionPreco_2")
        self.actionProduto = QAction(Chickie)
        self.actionProduto.setObjectName(u"actionProduto")
        self.actionAtualizarCategoria = QAction(Chickie)
        self.actionAtualizarCategoria.setObjectName(u"actionAtualizarCategoria")
        self.actionAtualizarEntregador = QAction(Chickie)
        self.actionAtualizarEntregador.setObjectName(u"actionAtualizarEntregador")
        self.actionAtualizarFeedback = QAction(Chickie)
        self.actionAtualizarFeedback.setObjectName(u"actionAtualizarFeedback")
        self.actionAtualizarFuncionario = QAction(Chickie)
        self.actionAtualizarFuncionario.setObjectName(u"actionAtualizarFuncionario")
        self.actionAtualizarZonaDeEntrega = QAction(Chickie)
        self.actionAtualizarZonaDeEntrega.setObjectName(u"actionAtualizarZonaDeEntrega")
        self.actionCliente_2 = QAction(Chickie)
        self.actionCliente_2.setObjectName(u"actionCliente_2")
        self.actionAtualizarPreco = QAction(Chickie)
        self.actionAtualizarPreco.setObjectName(u"actionAtualizarPreco")
        self.actionAtualizarPedido = QAction(Chickie)
        self.actionAtualizarPedido.setObjectName(u"actionAtualizarPedido")
        self.actionRemoverPreco = QAction(Chickie)
        self.actionRemoverPreco.setObjectName(u"actionRemoverPreco")
        self.actionRemoverProduto = QAction(Chickie)
        self.actionRemoverProduto.setObjectName(u"actionRemoverProduto")
        self.actionRemoverEntregador = QAction(Chickie)
        self.actionRemoverEntregador.setObjectName(u"actionRemoverEntregador")
        self.actionRemoverFuncionario = QAction(Chickie)
        self.actionRemoverFuncionario.setObjectName(u"actionRemoverFuncionario")
        self.actionRemoverMetodoDePagamento = QAction(Chickie)
        self.actionRemoverMetodoDePagamento.setObjectName(u"actionRemoverMetodoDePagamento")
        self.actionRemoverCategoria = QAction(Chickie)
        self.actionRemoverCategoria.setObjectName(u"actionRemoverCategoria")
        self.actionRemoverZonaDeEntrega = QAction(Chickie)
        self.actionRemoverZonaDeEntrega.setObjectName(u"actionRemoverZonaDeEntrega")
        self.actionHistorico = QAction(Chickie)
        self.actionHistorico.setObjectName(u"actionHistorico")
        self.actionObterAjuda = QAction(Chickie)
        self.actionObterAjuda.setObjectName(u"actionObterAjuda")
        self.actionCompartilharIdeias = QAction(Chickie)
        self.actionCompartilharIdeias.setObjectName(u"actionCompartilharIdeias")
        self.actionSobreOChickie = QAction(Chickie)
        self.actionSobreOChickie.setObjectName(u"actionSobreOChickie")
        self.centralwidget = QWidget(Chickie)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout.addWidget(self.lineEdit_7)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        Chickie.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Chickie)
        self.statusbar.setObjectName(u"statusbar")
        Chickie.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(Chickie)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        self.menuNovo = QMenu(self.menubar)
        self.menuNovo.setObjectName(u"menuNovo")
        self.menuAtualizar = QMenu(self.menubar)
        self.menuAtualizar.setObjectName(u"menuAtualizar")
        self.menuRemover = QMenu(self.menubar)
        self.menuRemover.setObjectName(u"menuRemover")
        self.menuHistorico = QMenu(self.menubar)
        self.menuHistorico.setObjectName(u"menuHistorico")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        Chickie.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNovo.menuAction())
        self.menubar.addAction(self.menuAtualizar.menuAction())
        self.menubar.addAction(self.menuRemover.menuAction())
        self.menubar.addAction(self.menuHistorico.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuNovo.addAction(self.actionNovaCategoria)
        self.menuNovo.addAction(self.actionNovoEntregador)
        self.menuNovo.addAction(self.actionNovoFuncionario)
        self.menuNovo.addAction(self.actionNovoMetodoDePagamento)
        self.menuNovo.addAction(self.actionNovaZonaDeEntrega)
        self.menuNovo.addAction(self.actionNovoCliente)
        self.menuNovo.addAction(self.actionNovoPreco)
        self.menuNovo.addAction(self.actionNovoPedido)
        self.menuAtualizar.addAction(self.actionAtualizarCategoria)
        self.menuAtualizar.addAction(self.actionAtualizarEntregador)
        self.menuAtualizar.addAction(self.actionAtualizarFeedback)
        self.menuAtualizar.addAction(self.actionAtualizarFuncionario)
        self.menuAtualizar.addAction(self.actionAtualizarZonaDeEntrega)
        self.menuAtualizar.addAction(self.actionAtualizarPreco)
        self.menuAtualizar.addAction(self.actionAtualizarPedido)
        self.menuRemover.addAction(self.actionRemoverCategoria)
        self.menuRemover.addAction(self.actionRemoverEntregador)
        self.menuRemover.addAction(self.actionRemoverFuncionario)
        self.menuRemover.addAction(self.actionRemoverMetodoDePagamento)
        self.menuRemover.addAction(self.actionRemoverZonaDeEntrega)
        self.menuRemover.addAction(self.actionRemoverPreco)
        self.menuRemover.addAction(self.actionRemoverProduto)
        self.menuHistorico.addAction(self.actionHistorico)
        self.menuSobre.addAction(self.actionObterAjuda)
        self.menuSobre.addAction(self.actionCompartilharIdeias)
        self.menuSobre.addSeparator()
        self.menuSobre.addAction(self.actionSobreOChickie)

        self.retranslateUi(Chickie)

        QMetaObject.connectSlotsByName(Chickie)
    # setupUi

    def retranslateUi(self, Chickie):
        Chickie.setWindowTitle(QCoreApplication.translate("Chickie", u"Chickie", None))
        self.actionCategoria.setText(QCoreApplication.translate("Chickie", u"Categoria", None))
        self.actionNovaCategoria.setText(QCoreApplication.translate("Chickie", u"Categoria", None))
        self.actionNovoEntregador.setText(QCoreApplication.translate("Chickie", u"Entregador", None))
        self.actionFeedback.setText(QCoreApplication.translate("Chickie", u"Feedback", None))
        self.actionNovoFuncionario.setText(QCoreApplication.translate("Chickie", u"Funcion\u00e1rio", None))
        self.actionNovoMetodoDePagamento.setText(QCoreApplication.translate("Chickie", u"M\u00e9todo de pagamento", None))
        self.actionNovaZonaDeEntrega.setText(QCoreApplication.translate("Chickie", u"Zona de entrega", None))
        self.actionNovoCliente.setText(QCoreApplication.translate("Chickie", u"Cliente", None))
        self.actionPedido.setText(QCoreApplication.translate("Chickie", u"Pedido", None))
        self.actionNovoPreco.setText(QCoreApplication.translate("Chickie", u"Pre\u00e7o", None))
        self.actionNovoPedido.setText(QCoreApplication.translate("Chickie", u"Pedido", None))
        self.actionPreco_2.setText(QCoreApplication.translate("Chickie", u"Pre\u00e7o", None))
        self.actionProduto.setText(QCoreApplication.translate("Chickie", u"Produto", None))
        self.actionAtualizarCategoria.setText(QCoreApplication.translate("Chickie", u"Categoria", None))
        self.actionAtualizarEntregador.setText(QCoreApplication.translate("Chickie", u"Entregador", None))
        self.actionAtualizarFeedback.setText(QCoreApplication.translate("Chickie", u"Feedback", None))
        self.actionAtualizarFuncionario.setText(QCoreApplication.translate("Chickie", u"Funcion\u00e1rio", None))
        self.actionAtualizarZonaDeEntrega.setText(QCoreApplication.translate("Chickie", u"Zona de Entrega", None))
        self.actionCliente_2.setText(QCoreApplication.translate("Chickie", u"Cliente", None))
        self.actionAtualizarPreco.setText(QCoreApplication.translate("Chickie", u"Pre\u00e7o", None))
        self.actionAtualizarPedido.setText(QCoreApplication.translate("Chickie", u"Pedido", None))
        self.actionRemoverPreco.setText(QCoreApplication.translate("Chickie", u"Pre\u00e7o", None))
        self.actionRemoverProduto.setText(QCoreApplication.translate("Chickie", u"Produto", None))
        self.actionRemoverEntregador.setText(QCoreApplication.translate("Chickie", u"Entregador", None))
        self.actionRemoverFuncionario.setText(QCoreApplication.translate("Chickie", u"Funcion\u00e1rio", None))
        self.actionRemoverMetodoDePagamento.setText(QCoreApplication.translate("Chickie", u"M\u00e9todo de pagamento", None))
        self.actionRemoverCategoria.setText(QCoreApplication.translate("Chickie", u"Categoria", None))
        self.actionRemoverZonaDeEntrega.setText(QCoreApplication.translate("Chickie", u"Zona de entrega", None))
        self.actionHistorico.setText(QCoreApplication.translate("Chickie", u"Historico de vendas", None))
        self.actionObterAjuda.setText(QCoreApplication.translate("Chickie", u"Obter ajuda", None))
        self.actionCompartilharIdeias.setText(QCoreApplication.translate("Chickie", u"Compartilhar ideias e comentarios", None))
        self.actionSobreOChickie.setText(QCoreApplication.translate("Chickie", u"Sobre o Chickie", None))
        self.label.setText(QCoreApplication.translate("Chickie", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("Chickie", u"Cargo", None))
        self.label_4.setText(QCoreApplication.translate("Chickie", u"E-mail", None))
        self.label_3.setText(QCoreApplication.translate("Chickie", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("Chickie", u"Senha", None))
        self.label_5.setText(QCoreApplication.translate("Chickie", u"Telefone", None))
        self.label_6.setText(QCoreApplication.translate("Chickie", u"Celular", None))
        self.pushButton.setText(QCoreApplication.translate("Chickie", u"Salvar", None))
        self.menuNovo.setTitle(QCoreApplication.translate("Chickie", u"Novo", None))
        self.menuAtualizar.setTitle(QCoreApplication.translate("Chickie", u"Atualizar", None))
        self.menuRemover.setTitle(QCoreApplication.translate("Chickie", u"Remover", None))
        self.menuHistorico.setTitle(QCoreApplication.translate("Chickie", u"Hist\u00f3rico", None))
        self.menuSobre.setTitle(QCoreApplication.translate("Chickie", u"Sobre", None))
    # retranslateUi

