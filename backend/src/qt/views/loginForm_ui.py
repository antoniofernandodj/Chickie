# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u".QLineEdit {\n"
"  background-color: #ffffff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"  background-color: #ddd\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame {\n"
"  border: 0px;\n"
"}\n"
"\n"
".QLineEdit {\n"
"  border: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.labelChikie = QLabel(self.frame)
        self.labelChikie.setObjectName(u"labelChikie")

        self.verticalLayout_2.addWidget(self.labelChikie, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.labelLogin = QLabel(self.frame)
        self.labelLogin.setObjectName(u"labelLogin")

        self.verticalLayout_2.addWidget(self.labelLogin, 0, Qt.AlignHCenter)

        self.lineEditLogin = QLineEdit(self.frame)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.lineEditLogin.setMinimumSize(QSize(0, 40))
        self.lineEditLogin.setMaxLength(30)
        self.lineEditLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEditLogin)

        self.labelSenha = QLabel(self.frame)
        self.labelSenha.setObjectName(u"labelSenha")

        self.verticalLayout_2.addWidget(self.labelSenha, 0, Qt.AlignHCenter)

        self.lineEditSenha = QLineEdit(self.frame)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        self.lineEditSenha.setMinimumSize(QSize(0, 40))
        self.lineEditSenha.setMaxLength(30)
        self.lineEditSenha.setEchoMode(QLineEdit.Password)
        self.lineEditSenha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEditSenha)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButtonEntrar = QPushButton(self.frame)
        self.pushButtonEntrar.setObjectName(u"pushButtonEntrar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEntrar.sizePolicy().hasHeightForWidth())
        self.pushButtonEntrar.setSizePolicy(sizePolicy)
        self.pushButtonEntrar.setBaseSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.pushButtonEntrar)

        self.pushButtonCadastrar = QPushButton(self.frame)
        self.pushButtonCadastrar.setObjectName(u"pushButtonCadastrar")

        self.verticalLayout_2.addWidget(self.pushButtonCadastrar)

        self.pushButtonEsqueciASenha = QPushButton(self.frame)
        self.pushButtonEsqueciASenha.setObjectName(u"pushButtonEsqueciASenha")

        self.verticalLayout_2.addWidget(self.pushButtonEsqueciASenha)

        self.verticalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login - Chickie", None))
        self.labelChikie.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Chickie</span></p></body></html>", None))
        self.labelLogin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Login</span></p></body></html>", None))
        self.lineEditLogin.setText("")
        self.lineEditLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu username de cadastro (ou email)", None))
        self.labelSenha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha</span></p></body></html>", None))
        self.lineEditSenha.setText("")
        self.lineEditSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.pushButtonEntrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.pushButtonCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastre-se", None))
        self.pushButtonEsqueciASenha.setText(QCoreApplication.translate("MainWindow", u"Esqueci a senha", None))
    # retranslateUi

