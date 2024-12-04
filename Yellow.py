import io
import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>806</width>
    <height>562</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>470</y>
      <width>281</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Нажми меня!</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>806</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Yellow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.run)


        self.point = []
        self.flag_draw = False
        self.key = None


    def run(self):
        self.key = 1
        self.point = [randint(30, 776), randint(30, 532)]
        self.flag_draw = True
        self.update()


    def paintEvent(self, event):
        if self.flag_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            side = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            if self.key == 1:
                self.qp.drawEllipse(QPointF(self.point[0], self.point[1]), side, side)

            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())
