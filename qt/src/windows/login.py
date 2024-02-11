from PySide6.QtWidgets import QMainWindow
from src.controllers import LoginController
from src.services import FileService as FS

# from PySide6.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self, app):
        from src.views.loginForm_ui import Ui_MainWindow as LoginView

        super().__init__()

        self.app = app

        self.view = LoginView()
        self.view.setupUi(self)

        self.setStyleSheet(FS.get('src/styles/main-window.qss'))
        self.view.frame.setStyleSheet(FS.get('src/styles/all.qss'))
        self.view.centralwidget.setStyleSheet(FS.get('src/styles/login.qss'))

        self.resize(450, 600)

        self.controller = LoginController(self.view, self.app, self)

        self.controller.setup()
        self.view.action_sair.triggered.connect(self.app.exit)

        """
        Eventos de Mouse:

        mousePressEvent: Quando um botão do mouse é
        pressionado.
        mouseReleaseEvent: Quando um botão do mouse é liberado após ser
        pressionado. mouseMoveEvent: Quando o mouse é movido dentro
        da área do widget. mouseDoubleClickEvent: Quando um botão
        do mouse é pressionado duas vezes rapidamente. Eventos de Teclado:

        keyPressEvent: Quando uma tecla é pressionada.
        keyReleaseEvent: Quando uma tecla é liberada após ser pressionada.
        Eventos de Foco:

        focusInEvent: Quando o widget obtém o foco
            (por exemplo, quando é clicado).

        focusOutEvent: Quando o widget perde o foco.
        Eventos de Redimensionamento:

        resizeEvent: Quando o widget é redimensionado.
        moveEvent: Quando o widget é movido para uma nova posição.
        Eventos de Pintura:

        paintEvent: Quando o widget precisa ser redesenhado.
        Eventos de Arrastar e Soltar (Drag and Drop):

        dragEnterEvent: Quando um objeto é arrastado e entra na área do widget.
        dragMoveEvent: Quando um objeto arrastado
            é movido sobre a área do widget.

        dragLeaveEvent: Quando um objeto arrastado deixa a área do widget.
        dropEvent: Quando um objeto arrastado é solto na área do widget.
        Eventos de Tempo:

        timerEvent: Quando um temporizador interno dispara.
        Esses são apenas alguns exemplos de eventos que podem ser tratados
        em uma aplicação Qt. Cada um desses eventos permite que você
        personalize a interação do usuário com a interface gráfica,
        capturando e respondendo a ações específicas. Através do
        tratamento de eventos, você pode criar interfaces de
        usuário altamente interativas e responsivas.
        """
