import sys, os
from service.track import TrackEngine
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

from widget.MainWindow import MainWindow

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'psg.myapp.objtrack.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


basedir = os.path.dirname(__file__)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'resource/logo.ico')))
    window = MainWindow()
    window.show()
    app.exec()