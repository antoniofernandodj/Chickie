# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedidos.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(818, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(800, 600))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_3 = QVBoxLayout(self.page_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.combo_box_status = QComboBox(self.frame_4)
        self.combo_box_status.setObjectName(u"combo_box_status")
        self.combo_box_status.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.combo_box_status)

        self.push_button_atualizar_status = QPushButton(self.frame_4)
        self.push_button_atualizar_status.setObjectName(u"push_button_atualizar_status")
        self.push_button_atualizar_status.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.push_button_atualizar_status)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push_button_visualizar_pedido = QPushButton(self.frame_5)
        self.push_button_visualizar_pedido.setObjectName(u"push_button_visualizar_pedido")
        self.push_button_visualizar_pedido.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.push_button_visualizar_pedido)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.push_button_concluido = QPushButton(self.frame_3)
        self.push_button_concluido.setObjectName(u"push_button_concluido")
        self.push_button_concluido.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.push_button_concluido)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.table_view_pedidos = QTableView(self.page_1)
        self.table_view_pedidos.setObjectName(u"table_view_pedidos")
        self.table_view_pedidos.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.table_view_pedidos)

        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.push_button_pedidos = QPushButton(self.frame_11)
        self.push_button_pedidos.setObjectName(u"push_button_pedidos")
        self.push_button_pedidos.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.push_button_pedidos)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_16)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.line_edit_data_hora = QLineEdit(self.frame_7)
        self.line_edit_data_hora.setObjectName(u"line_edit_data_hora")
        self.line_edit_data_hora.setMinimumSize(QSize(0, 30))
        self.line_edit_data_hora.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.line_edit_data_hora)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_16)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.line_edit_frete = QLineEdit(self.frame_8)
        self.line_edit_frete.setObjectName(u"line_edit_frete")
        self.line_edit_frete.setMinimumSize(QSize(0, 30))
        self.line_edit_frete.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.line_edit_frete)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 6)
        self.frame_9 = QFrame(self.frame_17)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_10.addWidget(self.label_5)

        self.line_edit_celular = QLineEdit(self.frame_9)
        self.line_edit_celular.setObjectName(u"line_edit_celular")
        self.line_edit_celular.setMinimumSize(QSize(0, 30))
        self.line_edit_celular.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.line_edit_celular)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.frame_17)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_12.addWidget(self.label_13)

        self.line_edit_status = QLineEdit(self.frame_13)
        self.line_edit_status.setObjectName(u"line_edit_status")
        self.line_edit_status.setMinimumSize(QSize(0, 30))
        self.line_edit_status.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.line_edit_status)


        self.horizontalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_12 = QFrame(self.frame_14)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 100))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_13.addWidget(self.label_2)

        self.text_edit_comentarios = QTextEdit(self.frame_12)
        self.text_edit_comentarios.setObjectName(u"text_edit_comentarios")
        self.text_edit_comentarios.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.text_edit_comentarios)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.table_view_itens_pedido = QTableView(self.frame_14)
        self.table_view_itens_pedido.setObjectName(u"table_view_itens_pedido")

        self.verticalLayout_11.addWidget(self.table_view_itens_pedido)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.line_edit_total = QLineEdit(self.frame_10)
        self.line_edit_total.setObjectName(u"line_edit_total")
        self.line_edit_total.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.line_edit_total)


        self.verticalLayout_8.addWidget(self.frame_10, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.push_button_atualizar_status.setText(QCoreApplication.translate("Dialog", u"Atualizar status", None))
        self.push_button_visualizar_pedido.setText(QCoreApplication.translate("Dialog", u"Visualizar pedido", None))
        self.push_button_concluido.setText(QCoreApplication.translate("Dialog", u"Conclu\u00eddo", None))
        self.push_button_pedidos.setText(QCoreApplication.translate("Dialog", u"Pedidos", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Data / Hora", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Frete", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Celular", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Observa\u00e7\u00f5es", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Total", None))
    # retranslateUi

