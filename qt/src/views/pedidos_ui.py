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
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1280, 700)
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
        self.frame_2 = QFrame(self.frame)
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
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.combo_box_status = QComboBox(self.frame_4)
        self.combo_box_status.setObjectName(u"combo_box_status")
        self.combo_box_status.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.combo_box_status)

        self.push_button_atualizar_status = QPushButton(self.frame_4)
        self.push_button_atualizar_status.setObjectName(u"push_button_atualizar_status")
        self.push_button_atualizar_status.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.push_button_atualizar_status)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.push_button_concluido = QPushButton(self.frame_3)
        self.push_button_concluido.setObjectName(u"push_button_concluido")
        self.push_button_concluido.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.push_button_concluido)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.table_view_pedidos = QTableView(self.frame)
        self.table_view_pedidos.setObjectName(u"table_view_pedidos")
        self.table_view_pedidos.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.table_view_pedidos)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.push_button_atualizar_status.setText(QCoreApplication.translate("Dialog", u"Atualizar status", None))
        self.push_button_concluido.setText(QCoreApplication.translate("Dialog", u"Conclu\u00eddo", None))
    # retranslateUi

