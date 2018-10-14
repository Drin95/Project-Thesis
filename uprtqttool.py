import sys

from PyQt4 import QtGui
from PyQt4.uic import *
from PyQt4.phonon import *

app = QtGui.QApplication(sys.argv)
widget = loadUi(r'C:\Users\andri\PycharmProjects\UPRT\Qt\testgui.ui')

media1 = Phonon.MediaSource(r'C:\Users\andri\PycharmProjects\UPRT\Data\Video\Snowy Trees.mp4')
widget.video1.load(media1)
widget.video1.play()

media2 = Phonon.MediaSource(r'C:\Users\andri\PycharmProjects\UPRT\Data\Video\Snowy Trees.mp4')
widget.video2.load(media2)
widget.video2.play()

widget.show()
sys.exit(app.exec())
