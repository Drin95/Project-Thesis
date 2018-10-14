import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np

# define the data
theTitle = "pyqtgraph plot"

txtfile = open(r'C:\Users\andri\PycharmProjects\UPRT\Data\Txt\transformed_puls.txt', 'r')
txtlist = [line.strip() for line in txtfile]
y = [int(i) for i in txtlist]
x = range(0, len(y))

# create plot
plt = pg.plot(x, y, title=theTitle, pen='r')
plt.showGrid(x=True, y=True)

# Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()