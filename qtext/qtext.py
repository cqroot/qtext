#!/usr/bin/env python3

import sys
from PySide6 import QtWidgets
from qtext.text_widget import TextWidget


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_widget = TextWidget()

        self.setLayout(QtWidgets.QVBoxLayout(self))
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.layout().addWidget(self.text_widget)


def main():
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
