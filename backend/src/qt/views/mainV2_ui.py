# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainV2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(773, 662)
        self.actionAtualizar = QAction(MainWindow)
        self.actionAtualizar.setObjectName(u"actionAtualizar")
        self.actionCadastro = QAction(MainWindow)
        self.actionCadastro.setObjectName(u"actionCadastro")
        self.actionRemover = QAction(MainWindow)
        self.actionRemover.setObjectName(u"actionRemover")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 40))
        self.tabCategoria = QWidget()
        self.tabCategoria.setObjectName(u"tabCategoria")
        self.verticalLayout_2 = QVBoxLayout(self.tabCategoria)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelNovaCategoriaProduto = QLabel(self.tabCategoria)
        self.labelNovaCategoriaProduto.setObjectName(u"labelNovaCategoriaProduto")
        self.labelNovaCategoriaProduto.setMinimumSize(QSize(0, 100))

        self.verticalLayout_2.addWidget(self.labelNovaCategoriaProduto, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.tabCategoria)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelNomeCategoriaProduto = QLabel(self.frame)
        self.labelNomeCategoriaProduto.setObjectName(u"labelNomeCategoriaProduto")

        self.verticalLayout_9.addWidget(self.labelNomeCategoriaProduto, 0, Qt.AlignHCenter)

        self.lineEditNomeCategoriaProduto = QLineEdit(self.frame)
        self.lineEditNomeCategoriaProduto.setObjectName(u"lineEditNomeCategoriaProduto")

        self.verticalLayout_9.addWidget(self.lineEditNomeCategoriaProduto)

        self.labelDescricaoCategoriaProduto = QLabel(self.frame)
        self.labelDescricaoCategoriaProduto.setObjectName(u"labelDescricaoCategoriaProduto")

        self.verticalLayout_9.addWidget(self.labelDescricaoCategoriaProduto, 0, Qt.AlignHCenter)

        self.plainTextEditDescricaoCategoriaProduto = QPlainTextEdit(self.frame)
        self.plainTextEditDescricaoCategoriaProduto.setObjectName(u"plainTextEditDescricaoCategoriaProduto")

        self.verticalLayout_9.addWidget(self.plainTextEditDescricaoCategoriaProduto)


        self.verticalLayout_2.addWidget(self.frame)

        self.pushButtonCadastrarCategoriaProduto = QPushButton(self.tabCategoria)
        self.pushButtonCadastrarCategoriaProduto.setObjectName(u"pushButtonCadastrarCategoriaProduto")
        self.pushButtonCadastrarCategoriaProduto.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.pushButtonCadastrarCategoriaProduto)

        self.tabWidget.addTab(self.tabCategoria, "")
        self.tabProduto = QWidget()
        self.tabProduto.setObjectName(u"tabProduto")
        self.verticalLayout_7 = QVBoxLayout(self.tabProduto)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.labelNovoProduto = QLabel(self.tabProduto)
        self.labelNovoProduto.setObjectName(u"labelNovoProduto")
        self.labelNovoProduto.setMinimumSize(QSize(0, 100))

        self.verticalLayout_7.addWidget(self.labelNovoProduto, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.tabProduto)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelCategoriaProduto = QLabel(self.frame_6)
        self.labelCategoriaProduto.setObjectName(u"labelCategoriaProduto")

        self.verticalLayout_10.addWidget(self.labelCategoriaProduto)

        self.comboBoxCategoriaProduto = QComboBox(self.frame_6)
        self.comboBoxCategoriaProduto.addItem("")
        self.comboBoxCategoriaProduto.setObjectName(u"comboBoxCategoriaProduto")

        self.verticalLayout_10.addWidget(self.comboBoxCategoriaProduto)

        self.labelNomeProduto = QLabel(self.frame_6)
        self.labelNomeProduto.setObjectName(u"labelNomeProduto")

        self.verticalLayout_10.addWidget(self.labelNomeProduto)

        self.lineEditNomeProduto = QLineEdit(self.frame_6)
        self.lineEditNomeProduto.setObjectName(u"lineEditNomeProduto")

        self.verticalLayout_10.addWidget(self.lineEditNomeProduto)

        self.labelPrecoProduto = QLabel(self.frame_6)
        self.labelPrecoProduto.setObjectName(u"labelPrecoProduto")

        self.verticalLayout_10.addWidget(self.labelPrecoProduto)

        self.doubleSpinBoxPrecoProduto = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBoxPrecoProduto.setObjectName(u"doubleSpinBoxPrecoProduto")

        self.verticalLayout_10.addWidget(self.doubleSpinBoxPrecoProduto)

        self.labelDescricaoProduto = QLabel(self.frame_6)
        self.labelDescricaoProduto.setObjectName(u"labelDescricaoProduto")

        self.verticalLayout_10.addWidget(self.labelDescricaoProduto)

        self.textEditDescricaoProduto = QTextEdit(self.frame_6)
        self.textEditDescricaoProduto.setObjectName(u"textEditDescricaoProduto")

        self.verticalLayout_10.addWidget(self.textEditDescricaoProduto)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.pushButtonCadastrarProduto = QPushButton(self.tabProduto)
        self.pushButtonCadastrarProduto.setObjectName(u"pushButtonCadastrarProduto")
        self.pushButtonCadastrarProduto.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.pushButtonCadastrarProduto)

        self.tabWidget.addTab(self.tabProduto, "")
        self.tabPreco = QWidget()
        self.tabPreco.setObjectName(u"tabPreco")
        self.verticalLayout_3 = QVBoxLayout(self.tabPreco)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelNovoPreco = QLabel(self.tabPreco)
        self.labelNovoPreco.setObjectName(u"labelNovoPreco")
        self.labelNovoPreco.setMinimumSize(QSize(0, 0))
        self.labelNovoPreco.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.labelNovoPreco, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.tabPreco)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.labelProdutoPreco = QLabel(self.frame_8)
        self.labelProdutoPreco.setObjectName(u"labelProdutoPreco")

        self.verticalLayout_14.addWidget(self.labelProdutoPreco)

        self.comboBoxProdutoPreco = QComboBox(self.frame_8)
        self.comboBoxProdutoPreco.addItem("")
        self.comboBoxProdutoPreco.setObjectName(u"comboBoxProdutoPreco")

        self.verticalLayout_14.addWidget(self.comboBoxProdutoPreco)

        self.labelValorPreco = QLabel(self.frame_8)
        self.labelValorPreco.setObjectName(u"labelValorPreco")

        self.verticalLayout_14.addWidget(self.labelValorPreco)

        self.doubleSpinValorPreco = QDoubleSpinBox(self.frame_8)
        self.doubleSpinValorPreco.setObjectName(u"doubleSpinValorPreco")

        self.verticalLayout_14.addWidget(self.doubleSpinValorPreco)

        self.labelDiaDaSemanaPreco = QLabel(self.frame_8)
        self.labelDiaDaSemanaPreco.setObjectName(u"labelDiaDaSemanaPreco")

        self.verticalLayout_14.addWidget(self.labelDiaDaSemanaPreco)

        self.comboBoxDiaDaSemanaPreco = QComboBox(self.frame_8)
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.addItem("")
        self.comboBoxDiaDaSemanaPreco.setObjectName(u"comboBoxDiaDaSemanaPreco")

        self.verticalLayout_14.addWidget(self.comboBoxDiaDaSemanaPreco)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.pushButtonCadastrarPreco = QPushButton(self.tabPreco)
        self.pushButtonCadastrarPreco.setObjectName(u"pushButtonCadastrarPreco")
        self.pushButtonCadastrarPreco.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButtonCadastrarPreco)

        self.tabWidget.addTab(self.tabPreco, "")
        self.tabZonaEntrega = QWidget()
        self.tabZonaEntrega.setObjectName(u"tabZonaEntrega")
        self.verticalLayout_8 = QVBoxLayout(self.tabZonaEntrega)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelCadastroZonaEntrega = QLabel(self.tabZonaEntrega)
        self.labelCadastroZonaEntrega.setObjectName(u"labelCadastroZonaEntrega")
        self.labelCadastroZonaEntrega.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_8.addWidget(self.labelCadastroZonaEntrega, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.tabZonaEntrega)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelCidadeZonaEntrega = QLabel(self.frame_7)
        self.labelCidadeZonaEntrega.setObjectName(u"labelCidadeZonaEntrega")
        self.labelCidadeZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelCidadeZonaEntrega, 2, 1, 1, 1)

        self.labelTaxaZonaEntrega = QLabel(self.frame_7)
        self.labelTaxaZonaEntrega.setObjectName(u"labelTaxaZonaEntrega")
        self.labelTaxaZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelTaxaZonaEntrega, 6, 1, 1, 1)

        self.labelCEPZonaEntrega = QLabel(self.frame_7)
        self.labelCEPZonaEntrega.setObjectName(u"labelCEPZonaEntrega")
        self.labelCEPZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelCEPZonaEntrega, 6, 0, 1, 1)

        self.lineEditCEPZonaEntrega = QLineEdit(self.frame_7)
        self.lineEditCEPZonaEntrega.setObjectName(u"lineEditCEPZonaEntrega")
        self.lineEditCEPZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEditCEPZonaEntrega, 7, 0, 1, 1)

        self.doubleSpinBoxTaxaZonaEntrega = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBoxTaxaZonaEntrega.setObjectName(u"doubleSpinBoxTaxaZonaEntrega")

        self.gridLayout_5.addWidget(self.doubleSpinBoxTaxaZonaEntrega, 7, 1, 1, 1)

        self.comboBoxUFZonaEntrega = QComboBox(self.frame_7)
        self.comboBoxUFZonaEntrega.addItem("")
        self.comboBoxUFZonaEntrega.setObjectName(u"comboBoxUFZonaEntrega")

        self.gridLayout_5.addWidget(self.comboBoxUFZonaEntrega, 5, 1, 1, 1)

        self.lineEditBairroZonaEntrega = QLineEdit(self.frame_7)
        self.lineEditBairroZonaEntrega.setObjectName(u"lineEditBairroZonaEntrega")
        self.lineEditBairroZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEditBairroZonaEntrega, 5, 0, 1, 1)

        self.lineEditNomeZonaEntrega = QLineEdit(self.frame_7)
        self.lineEditNomeZonaEntrega.setObjectName(u"lineEditNomeZonaEntrega")
        self.lineEditNomeZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEditNomeZonaEntrega, 3, 0, 1, 1)

        self.labelBairroZonaEntrega = QLabel(self.frame_7)
        self.labelBairroZonaEntrega.setObjectName(u"labelBairroZonaEntrega")
        self.labelBairroZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelBairroZonaEntrega, 4, 0, 1, 1)

        self.lineEditCidadeZonaEntrega = QLineEdit(self.frame_7)
        self.lineEditCidadeZonaEntrega.setObjectName(u"lineEditCidadeZonaEntrega")
        self.lineEditCidadeZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEditCidadeZonaEntrega, 3, 1, 1, 1)

        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 1)

        self.labelUFZonaEntrega = QLabel(self.frame_7)
        self.labelUFZonaEntrega.setObjectName(u"labelUFZonaEntrega")
        self.labelUFZonaEntrega.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelUFZonaEntrega, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 0, 1, 2)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.pushButtonCadastrarZonaEntrega = QPushButton(self.tabZonaEntrega)
        self.pushButtonCadastrarZonaEntrega.setObjectName(u"pushButtonCadastrarZonaEntrega")
        self.pushButtonCadastrarZonaEntrega.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButtonCadastrarZonaEntrega)

        self.tabWidget.addTab(self.tabZonaEntrega, "")
        self.tabCliente = QWidget()
        self.tabCliente.setObjectName(u"tabCliente")
        self.gridLayout = QGridLayout(self.tabCliente)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonCadastrarCliente = QPushButton(self.tabCliente)
        self.pushButtonCadastrarCliente.setObjectName(u"pushButtonCadastrarCliente")
        self.pushButtonCadastrarCliente.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButtonCadastrarCliente, 4, 0, 1, 1)

        self.frame_2 = QFrame(self.tabCliente)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEditEmailCliente = QLineEdit(self.frame_2)
        self.lineEditEmailCliente.setObjectName(u"lineEditEmailCliente")
        self.lineEditEmailCliente.setMinimumSize(QSize(0, 0))
        self.lineEditEmailCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditEmailCliente, 2, 0, 1, 1)

        self.lineEditUsernameCliente = QLineEdit(self.frame_2)
        self.lineEditUsernameCliente.setObjectName(u"lineEditUsernameCliente")
        self.lineEditUsernameCliente.setMinimumSize(QSize(0, 0))
        self.lineEditUsernameCliente.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditUsernameCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditUsernameCliente, 2, 1, 1, 1)

        self.lineEditSenhaCliente = QLineEdit(self.frame_2)
        self.lineEditSenhaCliente.setObjectName(u"lineEditSenhaCliente")
        self.lineEditSenhaCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditSenhaCliente, 4, 0, 1, 2)

        self.lineEditNomeCliente = QLineEdit(self.frame_2)
        self.lineEditNomeCliente.setObjectName(u"lineEditNomeCliente")
        self.lineEditNomeCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditNomeCliente, 1, 0, 1, 2)

        self.lineEditCelularCliente = QLineEdit(self.frame_2)
        self.lineEditCelularCliente.setObjectName(u"lineEditCelularCliente")
        self.lineEditCelularCliente.setMinimumSize(QSize(200, 0))
        self.lineEditCelularCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditCelularCliente, 3, 0, 1, 1)

        self.lineEditTelefoneCliente = QLineEdit(self.frame_2)
        self.lineEditTelefoneCliente.setObjectName(u"lineEditTelefoneCliente")
        self.lineEditTelefoneCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEditTelefoneCliente, 3, 1, 1, 1)

        self.labelDadosCliente = QLabel(self.frame_2)
        self.labelDadosCliente.setObjectName(u"labelDadosCliente")
        self.labelDadosCliente.setMinimumSize(QSize(0, 40))
        self.labelDadosCliente.setMaximumSize(QSize(16777215, 50))
        self.labelDadosCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.labelDadosCliente, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 2, 1)

        self.frame_15 = QFrame(self.tabCliente)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEditComplementoCliente = QLineEdit(self.frame_15)
        self.lineEditComplementoCliente.setObjectName(u"lineEditComplementoCliente")
        self.lineEditComplementoCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditComplementoCliente, 2, 1, 1, 1)

        self.lineEditLogradouroCliente = QLineEdit(self.frame_15)
        self.lineEditLogradouroCliente.setObjectName(u"lineEditLogradouroCliente")
        self.lineEditLogradouroCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditLogradouroCliente, 1, 0, 1, 4)

        self.lineEditCEPCliente = QLineEdit(self.frame_15)
        self.lineEditCEPCliente.setObjectName(u"lineEditCEPCliente")
        self.lineEditCEPCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditCEPCliente, 3, 1, 1, 2)

        self.lineEditNumeroCliente = QLineEdit(self.frame_15)
        self.lineEditNumeroCliente.setObjectName(u"lineEditNumeroCliente")
        self.lineEditNumeroCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditNumeroCliente, 2, 0, 1, 1)

        self.lineEditCidadeCliente = QLineEdit(self.frame_15)
        self.lineEditCidadeCliente.setObjectName(u"lineEditCidadeCliente")
        self.lineEditCidadeCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditCidadeCliente, 3, 0, 1, 1)

        self.comboBoxUFCliente = QComboBox(self.frame_15)
        self.comboBoxUFCliente.setObjectName(u"comboBoxUFCliente")
        self.comboBoxUFCliente.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_2.addWidget(self.comboBoxUFCliente, 3, 3, 1, 1)

        self.lineEditBairroCliente = QLineEdit(self.frame_15)
        self.lineEditBairroCliente.setObjectName(u"lineEditBairroCliente")
        self.lineEditBairroCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditBairroCliente, 2, 2, 1, 2)

        self.labelEnderecoCliente = QLabel(self.frame_15)
        self.labelEnderecoCliente.setObjectName(u"labelEnderecoCliente")
        self.labelEnderecoCliente.setMinimumSize(QSize(0, 40))
        self.labelEnderecoCliente.setMaximumSize(QSize(16777215, 16777215))
        self.labelEnderecoCliente.setBaseSize(QSize(0, 0))
        self.labelEnderecoCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelEnderecoCliente, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.frame_15, 3, 0, 1, 1)

        self.labelCadastroCliente = QLabel(self.tabCliente)
        self.labelCadastroCliente.setObjectName(u"labelCadastroCliente")
        self.labelCadastroCliente.setMinimumSize(QSize(0, 100))
        self.labelCadastroCliente.setMaximumSize(QSize(16777215, 100))
        self.labelCadastroCliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCadastroCliente, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabCliente, "")
        self.tabFornecedor = QWidget()
        self.tabFornecedor.setObjectName(u"tabFornecedor")
        self.verticalLayout_4 = QVBoxLayout(self.tabFornecedor)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelNovoFornecedor = QLabel(self.tabFornecedor)
        self.labelNovoFornecedor.setObjectName(u"labelNovoFornecedor")
        self.labelNovoFornecedor.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_4.addWidget(self.labelNovoFornecedor, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.tabFornecedor)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEditCelularFornecedor = QLineEdit(self.frame_3)
        self.lineEditCelularFornecedor.setObjectName(u"lineEditCelularFornecedor")
        self.lineEditCelularFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditCelularFornecedor, 2, 1, 1, 1)

        self.lineEditEmailFornecedor = QLineEdit(self.frame_3)
        self.lineEditEmailFornecedor.setObjectName(u"lineEditEmailFornecedor")
        self.lineEditEmailFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditEmailFornecedor, 2, 0, 1, 1)

        self.lineEditNomeFornecedor = QLineEdit(self.frame_3)
        self.lineEditNomeFornecedor.setObjectName(u"lineEditNomeFornecedor")
        self.lineEditNomeFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditNomeFornecedor, 1, 0, 1, 1)

        self.lineEditUsernameFornecedor = QLineEdit(self.frame_3)
        self.lineEditUsernameFornecedor.setObjectName(u"lineEditUsernameFornecedor")
        self.lineEditUsernameFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditUsernameFornecedor, 1, 1, 1, 1)

        self.lineEditTelefoneFornecedor = QLineEdit(self.frame_3)
        self.lineEditTelefoneFornecedor.setObjectName(u"lineEditTelefoneFornecedor")
        self.lineEditTelefoneFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditTelefoneFornecedor, 3, 0, 1, 1)

        self.lineEditCNPJFornecedor = QLineEdit(self.frame_3)
        self.lineEditCNPJFornecedor.setObjectName(u"lineEditCNPJFornecedor")
        self.lineEditCNPJFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditCNPJFornecedor, 3, 1, 1, 1)

        self.lineEditSiteFornecedor = QLineEdit(self.frame_3)
        self.lineEditSiteFornecedor.setObjectName(u"lineEditSiteFornecedor")
        self.lineEditSiteFornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditSiteFornecedor, 4, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.pushButtonCadastrarFornecedor = QPushButton(self.tabFornecedor)
        self.pushButtonCadastrarFornecedor.setObjectName(u"pushButtonCadastrarFornecedor")

        self.verticalLayout_4.addWidget(self.pushButtonCadastrarFornecedor)

        self.tabWidget.addTab(self.tabFornecedor, "")
        self.tabFuncionario = QWidget()
        self.tabFuncionario.setObjectName(u"tabFuncionario")
        self.verticalLayout_5 = QVBoxLayout(self.tabFuncionario)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelNovoFuncionario = QLabel(self.tabFuncionario)
        self.labelNovoFuncionario.setObjectName(u"labelNovoFuncionario")
        self.labelNovoFuncionario.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_5.addWidget(self.labelNovoFuncionario, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.tabFuncionario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lineEditNomeFuncionario = QLineEdit(self.frame_4)
        self.lineEditNomeFuncionario.setObjectName(u"lineEditNomeFuncionario")
        self.lineEditNomeFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditNomeFuncionario)

        self.lineEditCargoFuncionario = QLineEdit(self.frame_4)
        self.lineEditCargoFuncionario.setObjectName(u"lineEditCargoFuncionario")
        self.lineEditCargoFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditCargoFuncionario)

        self.lineEditEmailFuncionario = QLineEdit(self.frame_4)
        self.lineEditEmailFuncionario.setObjectName(u"lineEditEmailFuncionario")
        self.lineEditEmailFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditEmailFuncionario)

        self.lineEditSenhaFuncionario = QLineEdit(self.frame_4)
        self.lineEditSenhaFuncionario.setObjectName(u"lineEditSenhaFuncionario")
        self.lineEditSenhaFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditSenhaFuncionario)

        self.lineEditTelefoneFuncionario = QLineEdit(self.frame_4)
        self.lineEditTelefoneFuncionario.setObjectName(u"lineEditTelefoneFuncionario")
        self.lineEditTelefoneFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditTelefoneFuncionario)

        self.lineEditCelularFuncionario = QLineEdit(self.frame_4)
        self.lineEditCelularFuncionario.setObjectName(u"lineEditCelularFuncionario")
        self.lineEditCelularFuncionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEditCelularFuncionario)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.pushButtonCadastrarFuncionario = QPushButton(self.tabFuncionario)
        self.pushButtonCadastrarFuncionario.setObjectName(u"pushButtonCadastrarFuncionario")

        self.verticalLayout_5.addWidget(self.pushButtonCadastrarFuncionario)

        self.tabWidget.addTab(self.tabFuncionario, "")
        self.tabPedido = QWidget()
        self.tabPedido.setObjectName(u"tabPedido")
        self.verticalLayout_6 = QVBoxLayout(self.tabPedido)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.tabPedido)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelCadastrarPedido = QLabel(self.frame_10)
        self.labelCadastrarPedido.setObjectName(u"labelCadastrarPedido")
        self.labelCadastrarPedido.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_16.addWidget(self.labelCadastrarPedido, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"#frame_11, #frame_12, #frame_5 {\n"
"  border: 0px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame_11)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14 {\n"
"  border: 0px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_14)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.doubleSpinBoxFretePedido = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBoxFretePedido.setObjectName(u"doubleSpinBoxFretePedido")

        self.gridLayout_4.addWidget(self.doubleSpinBoxFretePedido, 1, 0, 1, 1)

        self.checkBoxFretePedido = QCheckBox(self.frame_14)
        self.checkBoxFretePedido.setObjectName(u"checkBoxFretePedido")

        self.gridLayout_4.addWidget(self.checkBoxFretePedido, 1, 2, 1, 1)

        self.labelFretePedido = QLabel(self.frame_14)
        self.labelFretePedido.setObjectName(u"labelFretePedido")

        self.gridLayout_4.addWidget(self.labelFretePedido, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.labelStatusPedido = QLabel(self.frame_5)
        self.labelStatusPedido.setObjectName(u"labelStatusPedido")

        self.verticalLayout_12.addWidget(self.labelStatusPedido)

        self.comboBoxStatusPedido = QComboBox(self.frame_5)
        self.comboBoxStatusPedido.addItem("")
        self.comboBoxStatusPedido.setObjectName(u"comboBoxStatusPedido")

        self.verticalLayout_12.addWidget(self.comboBoxStatusPedido)

        self.labelClientePedido = QLabel(self.frame_5)
        self.labelClientePedido.setObjectName(u"labelClientePedido")

        self.verticalLayout_12.addWidget(self.labelClientePedido)

        self.comboBoxClientePedido = QComboBox(self.frame_5)
        self.comboBoxClientePedido.addItem("")
        self.comboBoxClientePedido.setObjectName(u"comboBoxClientePedido")

        self.verticalLayout_12.addWidget(self.comboBoxClientePedido)

        self.textBrowserEndereco = QTextBrowser(self.frame_5)
        self.textBrowserEndereco.setObjectName(u"textBrowserEndereco")

        self.verticalLayout_12.addWidget(self.textBrowserEndereco)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.labelItemPedido = QLabel(self.frame_12)
        self.labelItemPedido.setObjectName(u"labelItemPedido")

        self.verticalLayout_17.addWidget(self.labelItemPedido, 0, Qt.AlignHCenter)

        self.comboBoxItemPedido = QComboBox(self.frame_12)
        self.comboBoxItemPedido.addItem("")
        self.comboBoxItemPedido.setObjectName(u"comboBoxItemPedido")

        self.verticalLayout_17.addWidget(self.comboBoxItemPedido)

        self.pushButtonAdicionarItemPedido = QPushButton(self.frame_12)
        self.pushButtonAdicionarItemPedido.setObjectName(u"pushButtonAdicionarItemPedido")

        self.verticalLayout_17.addWidget(self.pushButtonAdicionarItemPedido)

        self.listView = QListView(self.frame_12)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_17.addWidget(self.listView)


        self.horizontalLayout.addWidget(self.frame_12)


        self.verticalLayout_16.addWidget(self.frame_11)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.pushButtonCadastrarPedido = QPushButton(self.tabPedido)
        self.pushButtonCadastrarPedido.setObjectName(u"pushButtonCadastrarPedido")

        self.verticalLayout_6.addWidget(self.pushButtonCadastrarPedido)

        self.tabWidget.addTab(self.tabPedido, "")
        self.tabStatus = QWidget()
        self.tabStatus.setObjectName(u"tabStatus")
        self.verticalLayout_13 = QVBoxLayout(self.tabStatus)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelCadastroStatusPedido = QLabel(self.tabStatus)
        self.labelCadastroStatusPedido.setObjectName(u"labelCadastroStatusPedido")
        self.labelCadastroStatusPedido.setMinimumSize(QSize(0, 100))
        self.labelCadastroStatusPedido.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_13.addWidget(self.labelCadastroStatusPedido, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.tabStatus)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.labelNomeStatusPedido = QLabel(self.frame_9)
        self.labelNomeStatusPedido.setObjectName(u"labelNomeStatusPedido")

        self.verticalLayout_15.addWidget(self.labelNomeStatusPedido, 0, Qt.AlignHCenter)

        self.lineEditNomeStatusPedido = QLineEdit(self.frame_9)
        self.lineEditNomeStatusPedido.setObjectName(u"lineEditNomeStatusPedido")

        self.verticalLayout_15.addWidget(self.lineEditNomeStatusPedido)

        self.labelDescricaoStatusPedido = QLabel(self.frame_9)
        self.labelDescricaoStatusPedido.setObjectName(u"labelDescricaoStatusPedido")

        self.verticalLayout_15.addWidget(self.labelDescricaoStatusPedido, 0, Qt.AlignHCenter)

        self.textEditDescricaoStatusPedido = QTextEdit(self.frame_9)
        self.textEditDescricaoStatusPedido.setObjectName(u"textEditDescricaoStatusPedido")

        self.verticalLayout_15.addWidget(self.textEditDescricaoStatusPedido)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.pushButtonCadastrarStatusPedido = QPushButton(self.tabStatus)
        self.pushButtonCadastrarStatusPedido.setObjectName(u"pushButtonCadastrarStatusPedido")

        self.verticalLayout_13.addWidget(self.pushButtonCadastrarStatusPedido)

        self.tabWidget.addTab(self.tabStatus, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tabWidget.addTab(self.tab_14, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 773, 27))
        self.menuA_es = QMenu(self.menubar)
        self.menuA_es.setObjectName(u"menuA_es")
        self.menuHistorico = QMenu(self.menubar)
        self.menuHistorico.setObjectName(u"menuHistorico")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuA_es.menuAction())
        self.menubar.addAction(self.menuHistorico.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuA_es.addAction(self.actionAtualizar)
        self.menuA_es.addAction(self.actionCadastro)
        self.menuA_es.addAction(self.actionRemover)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chickie", None))
        self.actionAtualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar ...", None))
        self.actionCadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar ...", None))
        self.actionRemover.setText(QCoreApplication.translate("MainWindow", u"Remover ...", None))
        self.labelNovaCategoriaProduto.setText(QCoreApplication.translate("MainWindow", u"Nova categoria de produto", None))
        self.labelNomeCategoriaProduto.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lineEditNomeCategoriaProduto.setText("")
        self.labelDescricaoCategoriaProduto.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.pushButtonCadastrarCategoriaProduto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCategoria), QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.labelNovoProduto.setText(QCoreApplication.translate("MainWindow", u"Novo Produto", None))
        self.labelCategoriaProduto.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.comboBoxCategoriaProduto.setItemText(0, QCoreApplication.translate("MainWindow", u"Categoria A", None))

        self.labelNomeProduto.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lineEditNomeProduto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelPrecoProduto.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o padr\u00e3o", None))
        self.labelDescricaoProduto.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.textEditDescricaoProduto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.pushButtonCadastrarProduto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProduto), QCoreApplication.translate("MainWindow", u"Produto", None))
        self.labelNovoPreco.setText(QCoreApplication.translate("MainWindow", u"Novo Pre\u00e7o Excepcional", None))
        self.labelProdutoPreco.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.comboBoxProdutoPreco.setItemText(0, QCoreApplication.translate("MainWindow", u"Pizza tal", None))

        self.labelValorPreco.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.labelDiaDaSemanaPreco.setText(QCoreApplication.translate("MainWindow", u"Dia da semana", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(0, QCoreApplication.translate("MainWindow", u"Segunda", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(1, QCoreApplication.translate("MainWindow", u"Ter\u00e7a", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(2, QCoreApplication.translate("MainWindow", u"Quarta", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(3, QCoreApplication.translate("MainWindow", u"Quinta", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(4, QCoreApplication.translate("MainWindow", u"Sexta", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(5, QCoreApplication.translate("MainWindow", u"S\u00e1bado", None))
        self.comboBoxDiaDaSemanaPreco.setItemText(6, QCoreApplication.translate("MainWindow", u"Domingo", None))

        self.pushButtonCadastrarPreco.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPreco), QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.labelCadastroZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Zona de Entrega", None))
        self.labelCidadeZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.labelTaxaZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"Taxa", None))
        self.labelCEPZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEditCEPZonaEntrega.setPlaceholderText("")
        self.comboBoxUFZonaEntrega.setItemText(0, QCoreApplication.translate("MainWindow", u"RJ", None))

        self.comboBoxUFZonaEntrega.setPlaceholderText("")
        self.lineEditBairroZonaEntrega.setPlaceholderText("")
        self.lineEditNomeZonaEntrega.setPlaceholderText("")
        self.labelBairroZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lineEditCidadeZonaEntrega.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelUFZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.pushButtonCadastrarZonaEntrega.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabZonaEntrega), QCoreApplication.translate("MainWindow", u"Zona de Entrega", None))
        self.pushButtonCadastrarCliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lineEditEmailCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEditUsernameCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEditSenhaCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha (padr\u00e3o: 123456)", None))
        self.lineEditNomeCliente.setText("")
        self.lineEditNomeCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.lineEditCelularCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.lineEditTelefoneCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.labelDadosCliente.setText(QCoreApplication.translate("MainWindow", u"Dados Pessoais", None))
        self.lineEditComplementoCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.lineEditLogradouroCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.lineEditCEPCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEditNumeroCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.lineEditCidadeCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.lineEditBairroCliente.setText("")
        self.lineEditBairroCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.labelEnderecoCliente.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.labelCadastroCliente.setText(QCoreApplication.translate("MainWindow", u"Cadastro de cliente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCliente), QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.labelNovoFornecedor.setText(QCoreApplication.translate("MainWindow", u"Novo Fornecedor", None))
        self.lineEditCelularFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.lineEditEmailFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEditNomeFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lineEditUsernameFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEditTelefoneFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEditCNPJFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEditSiteFornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Site", None))
        self.pushButtonCadastrarFornecedor.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFornecedor), QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.labelNovoFuncionario.setText(QCoreApplication.translate("MainWindow", u"Novo Funcionario", None))
        self.lineEditNomeFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lineEditCargoFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.lineEditEmailFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEditSenhaFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEditTelefoneFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEditCelularFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.pushButtonCadastrarFuncionario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFuncionario), QCoreApplication.translate("MainWindow", u"Funcionario", None))
        self.labelCadastrarPedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Pedido", None))
        self.checkBoxFretePedido.setText(QCoreApplication.translate("MainWindow", u"Usar frete padr\u00e3o", None))
        self.labelFretePedido.setText(QCoreApplication.translate("MainWindow", u"Frete", None))
        self.labelStatusPedido.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.comboBoxStatusPedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Pendente", None))

        self.labelClientePedido.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.comboBoxClientePedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Marcelo", None))

        self.textBrowserEndereco.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rua bla bla bla</p></body></html>", None))
        self.labelItemPedido.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.comboBoxItemPedido.setItemText(0, QCoreApplication.translate("MainWindow", u"Pizza tal", None))

        self.pushButtonAdicionarItemPedido.setText(QCoreApplication.translate("MainWindow", u"Adicionar Item", None))
        self.pushButtonCadastrarPedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPedido), QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.labelCadastroStatusPedido.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Status de Pedido", None))
        self.labelNomeStatusPedido.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelDescricaoStatusPedido.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.pushButtonCadastrarStatusPedido.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatus), QCoreApplication.translate("MainWindow", u"Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Insumo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Contratos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Recebimentos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Pagamentos", None))
        self.menuA_es.setTitle(QCoreApplication.translate("MainWindow", u"A\u00e7\u00f5es", None))
        self.menuHistorico.setTitle(QCoreApplication.translate("MainWindow", u"Historico", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

