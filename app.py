import sys
from service.track import TrackEngine
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

from widget.MainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()