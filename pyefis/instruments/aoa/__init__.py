#  Copyright (c) 2023 Dan DeFord
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys
import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import pyavtools.fix as fix
import pyefis.hmi as hmi
from pyefis.instruments.NumericalDisplay import NumericalDisplay


class AoA(QWidget):

    def __init__(self, parent=None, fontsize=20):
        super(AoA, self).__init__(parent)

        self.setGeometry(10, 10, 180, 400)

        self.MarkerHeight = 8
        self.MarkerWidth = 100
        self.MarkerDistance = 1
        self.BorderThickness = 1

        self.RedLow         = QColor(130, 40, 40)
        self.RedHigh        = QColor(255, 40, 40)
        self.RedBorder      = QColor(200, 40, 40)

        self.YellowLow      = QColor(100, 100, 40)
        self.YellowHigh     = QColor(255, 255, 40)
        self.YellowBorder   = QColor(200, 200, 40)

        self.GreenLow       = QColor(40, 100, 40)
        self.GreenHigh      = QColor(40, 255, 40)
        self.GreenBorder    = QColor(40, 200, 40)

        self.WhiteLow       = QColor(100, 100, 100)
        self.WhiteHigh      = QColor(255, 255, 255)
        self.WhiteBorder    = QColor(200, 200, 200)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(self.RedBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.RedLow, Qt.SolidPattern))
        painter.drawRect(1, 0, self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.RedBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.RedHigh, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(1), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.YellowBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.YellowLow, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(2), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.YellowBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.YellowHigh, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(3), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(4), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(5), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenHigh, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(6), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.WhiteBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.WhiteHigh, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(7), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.WhiteBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.WhiteLow, Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(8), self.MarkerWidth, self.MarkerHeight)

    def setMarkerHeight(self, markerNumber):
        return markerNumber * (self.MarkerHeight + self.MarkerDistance + self.BorderThickness)
