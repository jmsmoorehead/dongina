from PyQt5 import QtWidgets, QtCore, QtGui
from fgmk import TileXtra

COLISIONLAYER = 3
EVENTSLAYER = 4

class LayerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.parent = parent

        self.VBox = QtWidgets.QVBoxLayout(self)
        self.VBox.setAlignment(QtCore.Qt.AlignTop)

        self.LabelLayer = QtWidgets.QLabel("Layer is: %d" % 0)
        self.VBox.addWidget(self.LabelLayer)
        self.ButtonLayer = []

        for i in range(len(TileXtra.LayersName)):
            self.ButtonLayer.append(
                QtWidgets.QPushButton(TileXtra.LayersName[i]))
            self.ButtonLayer[-1].setObjectName(TileXtra.LayersName[i])
            self.ButtonLayer[-1].clicked.connect(self.buttonLayerClicked)
            self.VBox.addWidget(self.ButtonLayer[-1])

        self.setMaximumHeight(180)
        self.show()

    def buttonLayerClicked(self):
        # print self.sender().objectName()
        if str(self.sender().objectName()) == TileXtra.LayersName[0]:
            self.changeLayerTo(0)
        elif str(self.sender().objectName()) == TileXtra.LayersName[1]:
            self.changeLayerTo(1)
        elif str(self.sender().objectName()) == TileXtra.LayersName[2]:
            self.changeLayerTo(2)
        elif str(self.sender().objectName()) == TileXtra.LayersName[3]:
            self.changeLayerTo(COLISIONLAYER)
        elif str(self.sender().objectName()) == TileXtra.LayersName[4]:
            self.changeLayerTo(EVENTSLAYER)

    def changeLayerTo(self, layerNumber):
        self.parent.changeLayerCurrent(layerNumber)

    def changeLayerView(self, layerNumber):
        self.LabelLayer.setText("Current: %s" %
                                TileXtra.LayersName[layerNumber])