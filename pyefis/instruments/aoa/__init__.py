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
    # First, let's define some things
    def __init__(self, parent=None, fontsize=20):
        super(AoA, self).__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.myparent = parent
        self.update_period = None
        self._aoa = 0
        self.item = fix.db.get_item("AOA")
        self.item.valueChanged[float].connect(self.setAOA)



        # Create a few variables that define the shape and properties
        # of each mark on the AoA indicator
        self.MarkerHeight = 8
        self.MarkerWidth = 20
        self.MarkerDistance = 2
        self.BorderThickness = 1

        # using the size of the markers, make the size of the canvas
        self.setGeometry(0, 0, self.MarkerWidth + 2, ((self.BorderThickness * 2) + self.MarkerHeight + self.MarkerDistance)*12)

        # create some re-usable colors for the various markers. High and Low will
        # indicate whether you have reached a threshold or not. Border color does not change
        self.RedLow         = QColor(130, 40, 40)
        self.RedHigh        = QColor(255, 40, 40)
        self.RedBorder      = QColor(200, 40, 40)

        self.YellowLow      = QColor(100, 100, 40)
        self.YellowHigh     = QColor(255, 255, 40)
        self.YellowBorder   = QColor(200, 200, 40)

        self.GreenLow       = QColor(40, 100, 40)
        self.GreenHigh      = QColor(40, 255, 40)
        self.GreenBorder    = QColor(40, 200, 40)

        self.BlueLow       = QColor(40, 50, 100)
        self.BlueHigh      = QColor(40, 90, 255)
        self.BlueBorder    = QColor(40, 90, 200)

    def setAOA(self, aoa):
        if aoa != self._aoa:
            self._aoa = aoa
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)


        painter.setPen(QPen(self.RedBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.RedLow if self._aoa < self.item.get_aux_value('Stall') else self.RedHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, 0, self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.RedBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.RedLow if self._aoa < self.item.get_aux_value('Stall') - 1.0 else self.RedHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(1), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.YellowBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.YellowLow if self._aoa < self.item.get_aux_value('Warn') else self.YellowHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(2), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.YellowBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.YellowLow if self._aoa < self.item.get_aux_value('Warn') - 1 else self.YellowHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(3), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 2 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(4), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 3 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(5), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 4 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(6), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 5 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(7), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 7 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(8), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa < self.item.get_aux_value('Warn') - 8 else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(9), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.BlueBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.BlueLow if self._aoa < self.item.get_aux_value('0g') + 3 else self.BlueHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(10), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.GreenBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.GreenLow if self._aoa <= self.item.get_aux_value('0g') else self.GreenHigh,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(11), self.MarkerWidth, self.MarkerHeight)

        painter.setPen(QPen(self.YellowBorder, self.BorderThickness, Qt.SolidLine))
        painter.setBrush(QBrush(self.YellowHigh if self._aoa < self.item.get_aux_value('0g') - 1 else self.YellowLow,
                                Qt.SolidPattern))
        painter.drawRect(1, self.setMarkerHeight(12), self.MarkerWidth, self.MarkerHeight)

    def setMarkerHeight(self, markerNumber):
        return markerNumber * (self.MarkerHeight + self.MarkerDistance + self.BorderThickness)
