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
    FULL_WIDTH = 50

    def __init__(self, parent=None, fontsize=20):
        super(AoA, self).__init__(parent)
        self.setStyleSheet("border: 0px")
        self.setFocusPolicy(Qt.NoFocus)
        self.fontsize = fontsize
        self._aoa = 0
        self.item = fix.db.get_item("AOA")
        self.item.valueChanged[float].connect(self.setAoA)
        self.item.oldChanged[bool].connect(self.repaint)
        self.item.badChanged[bool].connect(self.repaint)
        self.item.failChanged[bool].connect(self.repaint)

    # def paintEvent(self, event):
    #     w = self.width()
    #     h = self.height()
    #     dial = QPainter(self)
    #     dial.setRenderHint(QPainter.Antialiasing)
    #
    #     dial.fillRect(0, 0, w, h, Qt.black)
    #
    #     f = QFont
    #     fs = int(round(self.fontsize * w / self.FULL_WIDTH))
    #     f.setPixelSize(fs)
    #     fontMetrics = QFontMetricsF(f)
    #
    #     dialPen = QPen(QColor(Qt.white))
    #     dialPen.setWidth(2)
    #
    #     criticalAoA = QPen(QColor(Qt.red))
    #     criticalAoA.setWidth(6)


class AoA_Tape(QGraphicsView):
    def __init__(self, parent=None):
        super(AoA_Tape, self).__init__(parent)
        self.myparent = parent
        # p = self.parent.palette()
        # p = self.palette()

        self.screenColor = (10, 10, 10)
        self.setAutoFillBackground(True)
        # if self.screenColor:
        #     p.setColor(self.backgroundRole(), QColor(*self.screenColor))
        #     self.SetPalette(p)
        #     self.setAutoFillBackground(True)

        self.update_period = None
        self.setStyleSheet("background-color: rgba(30, 30, 30, 20%")
        #self.setStyleSheet("background: transparent")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.Antialiasing)
        self.setFocusPolicy(Qt.NoFocus)
        self.item = fix.db.get_item("AOA")
        self._aoa = self.item.value

        # AoA Angles
        self.ZeroG = self.item.get_aux_value("0g")
        self.Warn = self.item.get_aux_value("Warn")
        self.Stall = self.item.get_aux_value("Stall")

        self.max = int(round(self.Stall * 1.25))

        self.backgroundOpacity = 0.3
        self.foregroundOpacity = 0.6
        self.pph = 10
        self.fontsize = 15
        self.majorDiv = 10
        self.minorDiv = 5

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        self.markWidth = w / 5
        f = QFont()
        f.setPixelSize(self.fontsize)
        tape_height = self.max * self.pph + h
        tape_start = self.max * self.pph + h / 2

        dialPen = QPen(QColor(Qt.white))
        self.scene = QGraphicsScene(0, 0, w, tape_height)
        x = self.scene.addRect(0, 0, w, tape_height,
                               QPen(QColor(30, 30, 30)), QBrush(QColor(30, 30, 30)))
        x.setOpacity(self.backgroundOpacity)

        # Add angle markings
        # Green Bar
        r = QRectF(QPoint(0, -self.ZeroG * self.pph + tape_start),
                   QPoint(self.markWidth, -self.Warn * self.pph + tape_start))
        x = self.scene.addRect(r, QPen(QColor(0, 155, 0)), QBrush(QColor(0, 155, 0)))
        x.setOpacity(self.foregroundOpacity)

        # Yellow Bar

        def getAoA(self):
            return self._aoa

        def setAoA(self):
            if AoA != self._aoa:
                self._aoa = AoA
                self.redraw()

        aoa = property(getAoA, setAoA)

        def setAsOld(self, b):
            self.numerical_display.old = b

        def setAsBad(self, b):
            self.numerical_display.bad = b

        def setAsFail(self, b):
            self.numerical_display.fail = b
