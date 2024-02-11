# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_ingrediente_group_template.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize
)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QSizePolicy,
    QVBoxLayout
)

import uuid


def get_ingrediente_group(label):
    class Ui_Form(object):
        def setupUi(self, Form):
            if not Form.objectName():
                Form.setObjectName(str(uuid.uuid1))
            Form.resize(790, 504)
            self.frame = QFrame(Form)
            self.frame.setObjectName(str(uuid.uuid1))
            self.frame.setGeometry(QRect(330, 219, 241, 49))
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
            self.frame.setSizePolicy(sizePolicy)
            self.frame.setMinimumSize(QSize(0, 49))
            self.frame.setMaximumSize(QSize(16777215, 50))
            self.frame.setStyleSheet(u"#frame_radios, #frame_label {\n"
    "  border: 0px;\n"
    "}")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout = QHBoxLayout(self.frame)
            self.horizontalLayout.setObjectName(str(uuid.uuid1))
            self.frame_label = QFrame(self.frame)
            self.frame_label.setObjectName(str(uuid.uuid1))
            self.frame_label.setFrameShape(QFrame.StyledPanel)
            self.frame_label.setFrameShadow(QFrame.Raised)
            self.verticalLayout_2 = QVBoxLayout(self.frame_label)
            self.verticalLayout_2.setObjectName(str(uuid.uuid1))
            self.label = QLabel(self.frame_label)
            self.label.setObjectName(str(uuid.uuid1))
            self.label.setMaximumSize(QSize(16777215, 30))
            font = QFont()
            font.setBold(True)
            self.label.setFont(font)

            self.verticalLayout_2.addWidget(self.label)


            self.horizontalLayout.addWidget(self.frame_label)

            self.frame_radios = QFrame(self.frame)
            self.frame_radios.setObjectName(u"frame_radios")
            sizePolicy.setHeightForWidth(self.frame_radios.sizePolicy().hasHeightForWidth())
            self.frame_radios.setSizePolicy(sizePolicy)
            self.frame_radios.setMaximumSize(QSize(16777215, 47))
            self.frame_radios.setFrameShape(QFrame.StyledPanel)
            self.frame_radios.setFrameShadow(QFrame.Raised)
            self.gridLayout_2 = QGridLayout(self.frame_radios)
            self.gridLayout_2.setObjectName(str(uuid.uuid1))
            self.radio_nao = QRadioButton(self.frame_radios)
            self.radio_nao.setObjectName(str(uuid.uuid1))
            self.radio_nao.setMaximumSize(QSize(47, 16777215))

            self.gridLayout_2.addWidget(self.radio_nao, 0, 0, 1, 1)

            self.radio_sim = QRadioButton(self.frame_radios)
            self.radio_sim.setObjectName(str(uuid.uuid1))
            self.radio_sim.setMaximumSize(QSize(47, 16777215))

            self.gridLayout_2.addWidget(self.radio_sim, 0, 1, 1, 1)


            self.horizontalLayout.addWidget(self.frame_radios)


            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)
        # setupUi

        def retranslateUi(self, Form):
            id = str(uuid.uuid1)
            Form.setWindowTitle(QCoreApplication.translate(id, id, None))
            self.label.setText(QCoreApplication.translate(id, label, None))
            self.radio_nao.setText(QCoreApplication.translate(id, u"Sim", None))
            self.radio_sim.setText(QCoreApplication.translate(id, u"N\u00e3o", None))
        # retranslateUi

    return Ui_Form
