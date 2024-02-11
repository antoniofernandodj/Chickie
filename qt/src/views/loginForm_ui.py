# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(483, 600)
        MainWindow.setStyleSheet(u"")
        self.action_sair = QAction(MainWindow)
        self.action_sair.setObjectName(u"action_sair")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(420, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, 40, 60, 40)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")

        self.verticalLayout_2.addWidget(self.label_title, 0, Qt.AlignHCenter)

        self.label_login = QLabel(self.frame)
        self.label_login.setObjectName(u"label_login")

        self.verticalLayout_2.addWidget(self.label_login, 0, Qt.AlignHCenter)

        self.line_edit_login = QLineEdit(self.frame)
        self.line_edit_login.setObjectName(u"line_edit_login")
        self.line_edit_login.setMinimumSize(QSize(0, 40))
        self.line_edit_login.setStyleSheet(u"")
        self.line_edit_login.setMaxLength(30)
        self.line_edit_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.line_edit_login)

        self.label_senha = QLabel(self.frame)
        self.label_senha.setObjectName(u"label_senha")

        self.verticalLayout_2.addWidget(self.label_senha, 0, Qt.AlignHCenter)

        self.line_edit_senha = QLineEdit(self.frame)
        self.line_edit_senha.setObjectName(u"line_edit_senha")
        self.line_edit_senha.setMinimumSize(QSize(0, 40))
        self.line_edit_senha.setMaxLength(30)
        self.line_edit_senha.setEchoMode(QLineEdit.Password)
        self.line_edit_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.line_edit_senha)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.check_box_armazenar_senha = QCheckBox(self.frame_2)
        self.check_box_armazenar_senha.setObjectName(u"check_box_armazenar_senha")
        self.check_box_armazenar_senha.setMaximumSize(QSize(250, 100))

        self.gridLayout.addWidget(self.check_box_armazenar_senha, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.push_button_entrar = QPushButton(self.frame)
        self.push_button_entrar.setObjectName(u"push_button_entrar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_entrar.sizePolicy().hasHeightForWidth())
        self.push_button_entrar.setSizePolicy(sizePolicy)
        self.push_button_entrar.setMaximumSize(QSize(16777215, 50))
        self.push_button_entrar.setBaseSize(QSize(0, 0))
        self.push_button_entrar.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.push_button_entrar)

        self.push_button_esqueci_a_senha = QPushButton(self.frame)
        self.push_button_esqueci_a_senha.setObjectName(u"push_button_esqueci_a_senha")
        self.push_button_esqueci_a_senha.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.push_button_esqueci_a_senha)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 483, 22))
        self.menu_arquivo = QMenu(self.menubar)
        self.menu_arquivo.setObjectName(u"menu_arquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_arquivo.menuAction())
        self.menu_arquivo.addAction(self.action_sair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login - Chickie", None))
        self.action_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Chickie</span></p></body></html>", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Login</span></p></body></html>", None))
        self.line_edit_login.setText("")
        self.line_edit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu username (ou email)", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha</span></p></body></html>", None))
        self.line_edit_senha.setText("")
        self.line_edit_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.check_box_armazenar_senha.setText(QCoreApplication.translate("MainWindow", u"Armazenar senha localmente", None))
        self.push_button_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.push_button_esqueci_a_senha.setText(QCoreApplication.translate("MainWindow", u"Esqueci a senha", None))
        self.menu_arquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

