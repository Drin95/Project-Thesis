import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.phonon import *
from PyQt4.uic import *


app = QtGui.QApplication(sys.argv)
widget = loadUi(r'C:\Users\andri\PycharmProjects\SIM\Github_UPRT\monitor.ui')
#Gopro Video
media1 = Phonon.MediaSource(r'C:\Users\andri\PycharmProjects\UPRT\Data\Video\Snowy Trees.mp4')
widget.videoPlayer_1.load(media1)
widget.videoPlayer_1.play()

#Eye Tracker Video
media2 = Phonon.MediaSource(r'C:\Users\andri\PycharmProjects\UPRT\Data\Video\Snowy Trees.mp4')
widget.videoPlayer_2.load(media2)
widget.videoPlayer_2.play()

#Heart Frequency
media3 = Phonon.MediaSource(r'C:\Users\andri\PycharmProjects\UPRT\Data\Video\Snowy Trees.mp4')
widget.videoPlayer_3.load(media3)
widget.videoPlayer_3.play()



"""
class Debriefingtool(QDialog):
    def __init__(self):
        super(Debriefingtool, self).__init__()
        loadUi("pyqt4.ui", self)
        self.setWindowTitle("Debriefingtool for ZAV")

"""


widget.show()
sys.exit(app.exec_())
