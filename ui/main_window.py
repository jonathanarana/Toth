# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.urlLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.urlLineEdit.setText(_fromUtf8(""))
        self.urlLineEdit.setObjectName(_fromUtf8("urlLineEdit"))
        self.gridLayout.addWidget(self.urlLineEdit, 0, 1, 1, 1)
        self.downloadListWidget = QtGui.QListWidget(self.centralwidget)
        self.downloadListWidget.setObjectName(_fromUtf8("downloadListWidget"))
        self.gridLayout.addWidget(self.downloadListWidget, 1, 0, 1, 4)
        self.downloadPushButton = QtGui.QPushButton(self.centralwidget)
        self.downloadPushButton.setObjectName(_fromUtf8("downloadPushButton"))
        self.gridLayout.addWidget(self.downloadPushButton, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.outputDirLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.outputDirLineEdit.setText(_fromUtf8(""))
        self.outputDirLineEdit.setObjectName(_fromUtf8("outputDirLineEdit"))
        self.gridLayout.addWidget(self.outputDirLineEdit, 3, 1, 1, 1)
        self.browsePushButton = QtGui.QPushButton(self.centralwidget)
        self.browsePushButton.setObjectName(_fromUtf8("browsePushButton"))
        self.gridLayout.addWidget(self.browsePushButton, 3, 3, 1, 1)
        self.MP4Button = QtGui.QPushButton(self.centralwidget)
        self.MP4Button.setObjectName(_fromUtf8("MP4Button"))
        self.gridLayout.addWidget(self.MP4Button, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "URL:", None))
        self.urlLineEdit.setPlaceholderText(_translate("MainWindow", "URL del Video de YouTube", None))
        self.downloadPushButton.setText(_translate("MainWindow", "Música MP3", None))
        self.label_2.setText(_translate("MainWindow", "Guardar en:", None))
        self.outputDirLineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Carpeta de Salida</p></body></html>", None))
        self.outputDirLineEdit.setPlaceholderText(_translate("MainWindow", "Carpeta de Descarga", None))
        self.browsePushButton.setText(_translate("MainWindow", "Seleccionar", None))
        self.MP4Button.setText(_translate("MainWindow", "Vídeo MP4", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

