from PyQt5.QtWidgets import QFormLayout, QWidget, QLabel, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from settings import ASSETS_DIR


class ConnectGameWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):
        banner_image = QPixmap()
        banner_image.load(ASSETS_DIR + 'app/title.png')
        banner_image = banner_image.scaledToWidth(400)

        banner_image_label = QLabel('', self)
        banner_image_label.setAlignment(Qt.AlignCenter)
        banner_image_label.setPixmap(banner_image)

        # TODO: ADd form layout to main layout

        host_field_label = QLabel('Host', self)
        host_field_input = QPlainTextEdit()
        port_field_label = QLabel('Port', self)
        port_field_input = QPlainTextEdit()

        form_layout = QFormLayout()
        form_layout.addRow(host_field_label, host_field_input)
        form_layout.addRow(port_field_label, port_field_input)
        form_layout.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addWidget(banner_image_label)
        main_layout.addWidget(form_layout)

        self.setLayout(main_layout)
        self.show()
