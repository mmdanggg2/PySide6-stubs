from PySide6.QtCore import QPoint, QPointF


def multiplicationQPoint() -> None:
    p1 = QPoint(1, 1)
    p2 = QPoint(2, 2)
    assert p2 == 2 * p1
    assert p2 == p1 * 2
    p3 = QPoint(p1)
    p3 *= 2
    assert p3 == p2
    p3 *= 0.5
    assert p3 == p1


def divisionQPoint() -> None:
    p1 = QPoint(2, 2)
    assert p1 / 2 == QPoint(1, 1)
    assert p1 / 0.5 == QPoint(4, 4)
    p1 /= 2
    assert p1 == QPoint(1, 1)
    p1 /= 0.25
    assert p1 == QPoint(4, 4)


def multiplicationQPointF() -> None:
    p1 = QPointF(1.5, 1.5)
    p2 = QPointF(3, 3)
    assert p2 == 2 * p1
    assert p2 == p1 * 2
    p3 = QPointF(p1)
    p3 *= 2
    assert p3 == p2
    p3 *= 0.5
    assert p3 == p1


def divisionQPointF() -> None:
    p1 = QPointF(2, 2)
    assert p1 / 2 == QPointF(1, 1)
    assert p1 / 0.5 == QPointF(4, 4)
    p1 /= 2
    assert p1 == QPointF(1, 1)
    p1 /= 0.5
    assert p1 == QPointF(2, 2)


multiplicationQPoint()
divisionQPoint()
multiplicationQPointF()
divisionQPointF()
