from __future__ import annotations
from typing_extensions import override

from PySide6.QtCore import QModelIndex, QPersistentModelIndex
from PySide6.QtWidgets import QStyleOptionViewItem, QStyledItemDelegate, QWidget

class MyItemDelegate(QStyledItemDelegate):
    # createEditor can return None (this is the default implementation)
    @override
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex) -> QWidget | None:
        return super().createEditor(parent, option, index)

delegate = MyItemDelegate()
assert delegate.createEditor(QWidget(), QStyleOptionViewItem(), QModelIndex()) is None
