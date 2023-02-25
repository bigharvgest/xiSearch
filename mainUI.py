# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import myTextEdit
from ImageListWidgetUI import ImageListWidgetUI


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 0, 1000, 850))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 850))
        self.stackedWidget.setObjectName("stackedWidget")
        self.searchPageWidget = QtWidgets.QWidget()
        self.searchPageWidget.setObjectName("searchPageWidget")
        self.imgPathLabel = QtWidgets.QLabel(self.searchPageWidget)
        self.imgPathLabel.setGeometry(QtCore.QRect(10, 40, 138, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.imgPathLabel.setFont(font)
        self.imgPathLabel.setObjectName("imgPathLabel")
        self.imgPathEdit = myTextEdit.MyTextEdit(self.searchPageWidget)
        self.imgPathEdit.setGeometry(QtCore.QRect(150, 35, 700, 30))
        self.imgPathEdit.setObjectName("imgPathEdit")
        self.searchButton = QtWidgets.QPushButton(self.searchPageWidget)
        self.searchButton.setGeometry(QtCore.QRect(870, 35, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        # 图片流动布局
        # self.scrollArea = QtWidgets.QScrollArea(self.searchPageWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.searchPageWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 950, 700))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageListWidgetUI = ImageListWidgetUI()
        self.imageListWidgetUI.setGeometry(QtCore.QRect(10, 90, 950, 700))
        self.verticalLayout.addWidget(self.imageListWidgetUI)
        # 加载特征消息提示
        self.loadingMsgLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.loadingMsgLabel.setGeometry(QtCore.QRect(260, 300, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.loadingMsgLabel.setFont(font)
        self.loadingMsgLabel.setObjectName("loadingMsgLabel")
        self.loadingMsgLabel.setHidden(True)


        self.stackedWidget.addWidget(self.searchPageWidget)
        self.excutePageWidget = QtWidgets.QWidget()
        self.excutePageWidget.setObjectName("excutePageWidget")
        self.galleryPathLabel = QtWidgets.QLabel(self.excutePageWidget)
        self.galleryPathLabel.setGeometry(QtCore.QRect(10, 40, 138, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.galleryPathLabel.setFont(font)
        self.galleryPathLabel.setObjectName("galleryPathLabel")
        self.featurePathLabel = QtWidgets.QLabel(self.excutePageWidget)
        self.featurePathLabel.setGeometry(QtCore.QRect(10, 100, 138, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.featurePathLabel.setFont(font)
        self.featurePathLabel.setObjectName("featurePathLabel")
        self.galleryPathEdit = myTextEdit.MyTextEdit(self.excutePageWidget)
        self.galleryPathEdit.setGeometry(QtCore.QRect(180, 35, 700, 30))
        self.galleryPathEdit.setObjectName("galleryPathEdit")
        self.featurePathEdit = myTextEdit.MyTextEdit(self.excutePageWidget)
        self.featurePathEdit.setGeometry(QtCore.QRect(180, 95, 700, 30))
        self.featurePathEdit.setObjectName("featurePathEdit")
        self.excuteButton = QtWidgets.QPushButton(self.excutePageWidget)
        self.excuteButton.setGeometry(QtCore.QRect(400, 200, 100, 40))
        self.excuteButton.setObjectName("excuteButton")
        self.progressBar = QtWidgets.QProgressBar(self.excutePageWidget)
        self.progressBar.setGeometry(QtCore.QRect(230, 320, 500, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.processLabel = QtWidgets.QLabel(self.excutePageWidget)
        self.processLabel.setGeometry(QtCore.QRect(110, 320, 80, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.processLabel.setFont(font)
        self.processLabel.setObjectName("processLabel")
        self.stackedWidget.addWidget(self.excutePageWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 850))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.imgsearchPageButton = QtWidgets.QPushButton(self.frame)
        self.imgsearchPageButton.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.imgsearchPageButton.setObjectName("imgsearchPageButton")
        self.excutePageButton = QtWidgets.QPushButton(self.frame)
        self.excutePageButton.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.excutePageButton.setObjectName("excutePageButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1245, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "以图搜图   作者：xjhqre"))
        self.imgPathLabel.setText(_translate("MainWindow", "图片路径(可拖放)："))
        self.searchButton.setText(_translate("MainWindow", "搜索"))
        self.loadingMsgLabel.setText(_translate("MainWindow", "正在加载特征文件，请稍后"))
        self.galleryPathLabel.setText(_translate("MainWindow", "图片库地址："))
        self.featurePathLabel.setText(_translate("MainWindow", "特征文件保存地址："))
        self.excuteButton.setText(_translate("MainWindow", "提取特征"))
        self.processLabel.setText(_translate("MainWindow", "提取进度："))
        self.imgsearchPageButton.setText(_translate("MainWindow", "图片搜索"))
        self.excutePageButton.setText(_translate("MainWindow", "特征抽取"))
