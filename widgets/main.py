from PyQt5.QtWidgets import QStackedLayout, QWidget
from PyQt5.QtGui import QIcon

from widgets.connect import ConnectGameWindow
from settings import ASSETS_DIR


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.stack = None
        self.initUI()

    def initUI(self):
        self.stack = QStackedLayout(self)
        connect_game_window = ConnectGameWindow(self)
        self.stack.addWidget(connect_game_window)

        self.setStyleSheet('background-color: #07461B;')
        self.setWindowTitle('BANG! Online')
        self.setWindowIcon(QIcon(ASSETS_DIR + 'app/icon.png'))
        self.showFullScreen()
        self.show()
