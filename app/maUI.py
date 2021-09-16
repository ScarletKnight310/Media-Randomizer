from core import AnigaRan
from PyQt5 import QtCore, QtGui, QtWidgets
from core.InfoExtract import extractTitle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mangaButton = QtWidgets.QPushButton(self.centralwidget)
        self.mangaButton.setGeometry(QtCore.QRect(20, 110, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mangaButton.setFont(font)
        self.mangaButton.setObjectName("mangaButton")
        self.animeButton = QtWidgets.QPushButton(self.centralwidget)
        self.animeButton.setGeometry(QtCore.QRect(20, 210, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.animeButton.setFont(font)
        self.animeButton.setObjectName("animeButton")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 20, 400, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.mediaImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.mediaImage.setGeometry(QtCore.QRect(310, 20, 461, 341))
        self.mediaImage.setObjectName("mediaImage")
        self.lightNovelButton = QtWidgets.QPushButton(self.centralwidget)
        self.lightNovelButton.setGeometry(QtCore.QRect(20, 310, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lightNovelButton.setFont(font)
        self.lightNovelButton.setObjectName("lightNovelButton")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(20, 410, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomButton.setFont(font)
        self.randomButton.setObjectName("randomButton")
        self.mediaName = QtWidgets.QLabel(self.centralwidget)
        self.mediaName.setGeometry(QtCore.QRect(310, 370, 461, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mediaName.setFont(font)
        self.mediaName.setText("")
        self.mediaName.setObjectName("mediaName")
        self.mediaLink = QtWidgets.QTextEdit(self.centralwidget)
        self.mediaLink.setGeometry(QtCore.QRect(310, 500, 451, 40))
        font3 = QtGui.QFont()
        font3.setPointSize(16)
        self.mediaLink.setFont(font3)
        self.mediaLink.setObjectName("mediaLink")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.mangaButton.setText(_translate("MainWindow", "Manga"))
        self.animeButton.setText(_translate("MainWindow", "Anime"))
        self.titleLabel.setText(_translate("MainWindow", "Random Media"))
        self.lightNovelButton.setText(_translate("MainWindow", "Light Novel"))
        self.randomButton.setText(_translate("MainWindow", "I\'m Feeling Lucky"))

    def randomManga(self):
        self.titleLabel.setText("Random Manga")
        m = AnigaRan.randomAnime()
        self.mediaLink.setText(m)
        self.mediaName.setText(extractTitle(m))


    def randomAnime(self):
        self.titleLabel.setText("Random Anime")
        a = AnigaRan.randomAnime()
        self.mediaLink.setText(a)
        self.mediaName.setText(extractTitle(a))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # exc
    ui.mangaButton.clicked.connect(ui.randomManga)
    ui.animeButton.clicked.connect(ui.randomAnime)

    MainWindow.show()
    sys.exit(app.exec_())

