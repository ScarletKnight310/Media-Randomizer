from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mangaButton = QtWidgets.QPushButton(self.centralwidget)
        self.mangaButton.setGeometry(QtCore.QRect(220, 200, 381, 131))
        self.mangaButton.setObjectName("mangaButton")
        self.animeButton = QtWidgets.QPushButton(self.centralwidget)
        self.animeButton.setGeometry(QtCore.QRect(220, 60, 381, 131))
        self.animeButton.setObjectName("animeButton")
        self.mainAppText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.mainAppText.setGeometry(QtCore.QRect(80, 400, 641, 91))
        self.mainAppText.setObjectName("mainAppText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mangaButton.setText(_translate("MainWindow", "Manga"))
        self.animeButton.setText(_translate("MainWindow", "Anime"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


