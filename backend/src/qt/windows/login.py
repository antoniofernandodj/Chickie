from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import LoginController
from PySide6.QtCore import Qt

# from PySide6.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self, app, host):
        from src.qt.views.loginForm_ui import Ui_MainWindow as LoginView

        super().__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        """
        Qt.Window:
        # É a flag padrão que define a janela como uma janela normal.
        # A barra de título, botões de minimizar, maximizar e fechar estão
        presentes.
        # A janela é redimensionável.

        Qt.Dialog:
        # Especifica que a janela é um diálogo.
        # Uma barra de título menor é exibida.
        # Pode ter botões de minimizar e fechar.

        Qt.WindowStaysOnTopHint:
        # Mantém a janela sempre no topo de outras janelas.
        # Útil para diálogos importantes ou de notificação.

        Qt.WindowMinimizeButtonHint:
        # Exibe um botão de minimizar na barra de título.
        # Permite minimizar a janela para a barra de tarefas ou dock.

        Qt.WindowMaximizeButtonHint:
        # Exibe um botão de maximizar na barra de título.
        # Permite maximizar a janela para ocupar todo o espaço disponível
        na tela.

        Qt.WindowCloseButtonHint:
        # Exibe um botão de fechar na barra de título.
        # Permite fechar a janela.

        Qt.CustomizeWindowHint:
        # Permite personalizar a janela, ocultando ou exibindo certos
        elementos da barra de título.
        # Você pode combinar essa flag com outras para definir um
        comportamento específico.

        Qt.WindowTitleHint:
        # Exibe uma barra de título com o título da janela.
        # Esta flag é comumente usada, mas pode ser desativada para criar
        janelas sem barra de título.

        Qt.WindowContextHelpButtonHint:
        # Adiciona um botão de ajuda à barra de título.
        # Pode ser usado para fornecer informações de ajuda específicas
        para a janela.
        
        Qt.FramelessWindowHint:
        # Remove a barra de título e a moldura da janela.
        # Ideal para criar janelas personalizadas sem decorações padrão.

        Qt.Tool:
        # Define a janela como uma ferramenta, geralmente uma janela flutuante.
        # Pode ser usada para criar paletas ou janelas de configuração.

        Qt.SplashScreen:
        # Exibe a janela como uma tela de splash.
        # Geralmente usada para exibir uma tela temporária de
        carregamento ou introdução.

        Qt.ToolTip:
        # Especifica que a janela é uma dica de ferramenta.
        # Exibe a janela como uma dica flutuante quando o mouse
        passa sobre um widget.
        """
        self.host = host
        self.app = app

        self.view = LoginView()
        self.view.setupUi(self)
        self.resize(450, 600)

        self.controller = LoginController(
            view=self.view, app=self.app, window=self
        )  # ###

        self.controller.setup()
        self.view.actionSair.triggered.connect(self.exit)
        self.mousePos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.mousePos)

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def exit(self):
        self.app.exit()

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

    focusInEvent: Quando o widget obtém o foco (por exemplo, quando é clicado).
    focusOutEvent: Quando o widget perde o foco.
    Eventos de Redimensionamento:

    resizeEvent: Quando o widget é redimensionado.
    moveEvent: Quando o widget é movido para uma nova posição.
    Eventos de Pintura:

    paintEvent: Quando o widget precisa ser redesenhado.
    Eventos de Arrastar e Soltar (Drag and Drop):

    dragEnterEvent: Quando um objeto é arrastado e entra na área do widget.
    dragMoveEvent: Quando um objeto arrastado é movido sobre a área do widget.
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
