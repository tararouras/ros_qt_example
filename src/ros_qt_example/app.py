import sys
from ros_qt_example.window import Window
from ros_qt_example.ros_node import RosNode
from PyQt5 import QtWidgets

def run():
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    ros_node = RosNode()
    w.start(ros_node)
    sys.exit(app.exec_())
