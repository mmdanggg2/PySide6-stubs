"""Tests for QLineEdit."""
import string

from PySide6.QtWidgets import QApplication, QLineEdit

# test that QLineEdit.setText() accepts None as parameter
edit = QLineEdit()
edit.setText(None)
