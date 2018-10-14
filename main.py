import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtWidgets import QApplication, QDialog
from PyQt4.uic import loadUi



class debreefingtool(QDialog):
    def __init__(self):
        super(debreefingtool, self).__init__()
        loadUi(r'C:\Users\andri\PycharmProjects\UPRT\Qt\testgui.ui', self)



app = QApplication(sys.argv)
widget = debreefingtool()
widget.show()
sys.exit(app.exec_())
