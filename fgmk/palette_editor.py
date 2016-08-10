import os
from PyQt5 import QtGui, QtCore, QtWidgets
from fgmk import base_model, current_project, fifl

class PaletteFormat(base_model.BaseFormat):
    def __init__(self):
        base_model.BaseFormat.__init__(self)
        pass


class PaletteEditorWidget(QtWidgets.QDialog):
    def __init__(self, parent=None, ssettings={}, **kwargs):
        QtWidgets.QDialog.__init__(self, parent, **kwargs)

        self.pal = PaletteFormat()

        self.mainVBox = QtWidgets.QVBoxLayout(self)
        self.mainVBox.setAlignment(QtCore.Qt.AlignTop)
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        self.mainVBox.addWidget(scrollArea)
        insideScrollArea = QtWidgets.QWidget(scrollArea)
        scrollArea.setWidget(insideScrollArea)
        VBox = QtWidgets.QVBoxLayout(insideScrollArea)
        VBox.setAlignment(QtCore.Qt.AlignTop)
        insideScrollArea.setLayout(VBox)

        HBox=QtWidgets.QHBoxLayout()
        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.buttonClicked[QtWidgets.QAbstractButton].connect(self.buttonClicked)
        buttons=[{'name':'new' , 'id':0, 'objname':'new_pal' },
                 {'name':'open', 'id':1, 'objname':'open_pal'},
                 {'name':'save', 'id':2, 'objname':'save_pal'}]
        for b in buttons:
            button = QtWidgets.QPushButton(b['name'])
            button.setObjectName(b['objname'])
            self.buttonGroup.addButton(button, b['id'])
            HBox.addWidget(button)

        VBox.addLayout(HBox)

    def buttonClicked(self, button):
        if(button.objectName()=='open_pal'):
            self.openPalette()

    def openPalette(self):
        folder_to_open_to=""
        if(current_project.settings['gamefolder'] == ''):
            folder_to_open_to = os.path.expanduser('~')
        else:
            folder_to_open_to = os.path.join(current_project.settings['gamefolder'], fifl.LEVELS)

        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                        'Open File',
                        folder_to_open_to,
                        "JSON Palette (*.pal.json);;All Files (*)")[0]
        if(filename!=''):
            self.pal.load(filename)


if __name__ == "__main__":
    from sys import argv, exit

    a = QtWidgets.QApplication(argv)
    m = PaletteEditorWidget()
    a.processEvents()
    m.show()
    m.raise_()
    exit(a.exec_())
