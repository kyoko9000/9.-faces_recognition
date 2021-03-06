# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_9.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Screen = QtWidgets.QLabel(self.centralwidget)
        self.Screen.setGeometry(QtCore.QRect(9, 9, 901, 521))
        font = QtGui.QFont()
        font.setPointSize(100)
        self.Screen.setFont(font)
        self.Screen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Screen.setStyleSheet("background-color: rgb(115, 188, 255);")
        self.Screen.setFrameShape(QtWidgets.QFrame.Panel)
        self.Screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screen.setLineWidth(2)
        self.Screen.setMidLineWidth(0)
        self.Screen.setScaledContents(True)
        self.Screen.setAlignment(QtCore.Qt.AlignCenter)
        self.Screen.setObjectName("Screen")
        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(140, 530, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName("Button_start")
        self.Button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.Button_stop.setGeometry(QtCore.QRect(570, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_stop.setFont(font)
        self.Button_stop.setObjectName("Button_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Screen.setText(_translate("MainWindow", "screen"))
        self.Button_start.setText(_translate("MainWindow", "Start"))
        self.Button_stop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
