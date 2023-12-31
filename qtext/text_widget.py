#!/usr/bin/env python3

from PySide6 import QtWidgets


class TextWidget(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["key", "content"])

        self.horizontalHeader().resizeSection(0, 300)
        self.horizontalHeader().setStretchLastSection(True)
