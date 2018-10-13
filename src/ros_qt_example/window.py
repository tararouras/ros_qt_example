from ros_qt_example.example_ui import Ui_StackedWidget
from PyQt5 import QtGui, QtCore, QtWidgets


class Window(QtWidgets.QStackedWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

        self._ui = Ui_StackedWidget()
        self._ui.setupUi(self)
        self.setCurrentIndex(0)
        self._ui.goButton.clicked.connect(self._on_click)

        self._worker = None

    def closeEvent(self, *args, **kwargs):
        if self._worker:
            self._worker.stop()
        super(Window, self).closeEvent(*args, **kwargs)

    @QtCore.pyqtSlot()
    def _on_click(self):
        self.setCurrentIndex(1)
        self._worker.notify()

    def go_back(self):
        self.setCurrentIndex(0)

    def start(self, worker):
        self.show()
        self._worker = worker
        self._worker.start(self.go_back)

