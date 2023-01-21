from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from pytube import YouTube
import sys
import time



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1110, 686)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\youtube-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #000;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(320, 30, 471, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(450, 110, 201, 131))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(".\\YouTube-logo.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.lineEditLink = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLink.setGeometry(QtCore.QRect(180, 280, 621, 61))
        self.lineEditLink.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    border-radius: 6px;\n"
"    border: 2px solid white;\n"
"    padding: 2px;\n"
"}")
        self.lineEditLink.setObjectName("lineEditLink")
        self.labelLink = QtWidgets.QLabel(self.centralwidget)
        self.labelLink.setGeometry(QtCore.QRect(70, 285, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.labelLink.setFont(font)
        self.labelLink.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.labelLink.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLink.setObjectName("labelLink")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(840, 280, 151, 61))
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    border: 0;\n"
"    border-radius: 6px;\n"
"    background-color: #e81c41;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e81c30;\n"
"}")

        self.browseButton.setObjectName("browseButton")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(400, 450, 331, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(1)
        self.downloadButton.setFont(font)
        self.downloadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    border: 0;\n"
"    border-radius: 6px;\n"
"    background-color: #1422ba;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1475ba;\n"
"}")


        self.completeLabel = QtWidgets.QLabel(self.centralwidget)
        self.completeLabel.setGeometry(QtCore.QRect(340, 360, 471, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.completeLabel.setFont(font)
        self.completeLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.completeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.completeLabel.setObjectName("completeLabel")


        self.downloadButton.setObjectName("downloadButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video Downloader"))
        self.titleLabel.setText(_translate("MainWindow", "Youtube Video Downloader"))
        self.lineEditLink.setPlaceholderText(_translate("MainWindow", "Video Link..."))
        self.labelLink.setText(_translate("MainWindow", "Video Link:"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.completeLabel.setText(_translate("MainWindow", ""))
        self.downloadButton.setText(_translate("MainWindow", "Download"))

        # connect browse button to browse function
        self.browseButton.clicked.connect(self.browse)

        # connect browse button to browse function
        self.downloadButton.clicked.connect(self.start_download)

        self.download_thread = QThreadPool()
        
    def start_download(self):
        self.download_thread.start(self.download)


    def browse(self):
        self.video_path = QtWidgets.QFileDialog.getExistingDirectory()


    def download(self):
        
        try:
            link = self.lineEditLink.text()
            yt = YouTube(link)
            if link != "":
                self.completeLabel.setText("downloading...")
                yt.streams.get_highest_resolution().download(self.video_path)
                self.completeLabel.setText("Download completed successfully")
                time.sleep(3)
                self.completeLabel.setText("")

            else:
                pass
        except Exception as exc:
            pass

        link = self.lineEditLink.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
