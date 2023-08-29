from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from moc.mainwindow import Ui_MainWindow
import json


from store import trackEngine

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.BTN_LOAD.clicked.connect(self.btnLoadClicked)
    
    def btnLoadClicked(self):
        [path, ext] = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video", "D:\\Workspace\\Work\\OpenCV\\", "*.mp4")
        loops = trackEngine.run(path)
        text = json.dumps(loops, indent=1)
        self.EDIT_LOG.setPlainText(text)

