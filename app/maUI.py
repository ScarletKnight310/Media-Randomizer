from core import AnigaRan
from PyQt5 import QtCore, QtGui, QtWidgets

from core.InfoExtract import extractTitle, extractDesc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mangaButton = QtWidgets.QPushButton(self.centralwidget)
        self.mangaButton.setGeometry(QtCore.QRect(20, 130, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mangaButton.setFont(font)
        self.mangaButton.setObjectName("mangaButton")
        self.animeButton = QtWidgets.QPushButton(self.centralwidget)
        self.animeButton.setGeometry(QtCore.QRect(20, 230, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.animeButton.setFont(font)
        self.animeButton.setObjectName("animeButton")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.mediaImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.mediaImage.setGeometry(QtCore.QRect(310, 20, 671, 371))
        self.mediaImage.setObjectName("mediaImage")
        self.lightNovelButton = QtWidgets.QPushButton(self.centralwidget)
        self.lightNovelButton.setGeometry(QtCore.QRect(20, 330, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lightNovelButton.setFont(font)
        self.lightNovelButton.setObjectName("lightNovelButton")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(20, 430, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomButton.setFont(font)
        self.randomButton.setObjectName("randomButton")
        self.mediaName = QtWidgets.QLabel(self.centralwidget)
        self.mediaName.setGeometry(QtCore.QRect(310, 410, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mediaName.setFont(font)
        self.mediaName.setText("")
        self.mediaName.setObjectName("mediaName")
        self.mediaLink = QtWidgets.QTextEdit(self.centralwidget)
        self.mediaLink.setGeometry(QtCore.QRect(310, 670, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mediaLink.setFont(font)
        self.mediaLink.setObjectName("mediaLink")
        self.mediaDesc = QtWidgets.QLabel(self.centralwidget)
        self.mediaDesc.setGeometry(QtCore.QRect(310, 480, 671, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mediaDesc.setFont(font)
        self.mediaDesc.setText("")
        self.mediaDesc.setObjectName("mediaDesc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
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
        self.mediaLink.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                          "type=\"text/css\">\n "
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                          "font-size:16pt; font-weight:400; font-style:normal;\">\n "
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                          "text-indent:0px;\"><br /></p></body></html>"))

    def randomManga(self):
        self.titleLabel.setText("Random Manga")
        m = AnigaRan.randomAnime()
        self.mediaLink.setText(m)
        self.mediaName.setText(extractTitle(m))
        self.mediaDesc.setText(extractDesc(m))

    def randomAnime(self):
        self.titleLabel.setText("Random Anime")
        a = AnigaRan.randomAnime()
        self.mediaLink.setText(a)
        self.mediaName.setText(extractTitle(a))
        self.mediaDesc.setText(extractDesc(a))


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
