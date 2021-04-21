

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *




class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(843, 379)
        self.setStyleSheet(open("design/still.qss", "r").read())

        self.lbl_genel = QtWidgets.QLabel(self)
        self.lbl_genel.setGeometry(0,0,843,379)


        self.btn_weight = QtWidgets.QPushButton(self)
        self.btn_weight.setGeometry(QtCore.QRect(10, 10, 111, 41))
        icon = QtGui.QIcon("icons/weight.png")
        self.btn_weight.setIcon(icon)
        self.btn_weight.setIconSize(QSize(20,20))

        self.btn_cfg = QtWidgets.QPushButton(self)
        self.btn_cfg.setGeometry(QtCore.QRect(10, 60, 111, 41))
        icon = QtGui.QIcon("icons/config.png")
        self.btn_cfg.setIcon(icon)
        self.btn_cfg.setIconSize(QSize(20,20))



        self.btn_names = QtWidgets.QPushButton(self)
        self.btn_names.setGeometry(QtCore.QRect(10, 110, 111, 41))
        icon = QtGui.QIcon("icons/names.png")
        self.btn_names.setIcon(icon)
        self.btn_names.setIconSize(QSize(20,20))

        self.btn_video = QtWidgets.QPushButton(self)
        self.btn_video.setGeometry(QtCore.QRect(10, 189, 111, 41))
        icon = QtGui.QIcon("icons/video.png")
        self.btn_video.setIcon(icon)
        self.btn_video.setIconSize(QSize(20,20))

        self.btn_image = QtWidgets.QPushButton(self)
        self.btn_image.setGeometry(QtCore.QRect(10, 240, 111, 41))
        icon = QtGui.QIcon("icons/image.png")
        self.btn_image.setIcon(icon)
        self.btn_image.setIconSize(QSize(20,20))

        self.btn_videoBasla = QtWidgets.QPushButton(self)
        self.btn_videoBasla.setGeometry(QtCore.QRect(130, 190, 111, 41))

        self.btn_imageBasla = QtWidgets.QPushButton(self)
        self.btn_imageBasla.setGeometry(QtCore.QRect(130, 240, 111, 41))

        self.btn_webCamBasla = QtWidgets.QPushButton(self)
        self.btn_webCamBasla.setGeometry(QtCore.QRect(10, 290, 111, 41))
        icon = QtGui.QIcon("icons/webcam.png")
        self.btn_webCamBasla.setIcon(icon)
        self.btn_webCamBasla.setIconSize(QSize(20, 20))

        self.lbl_goruntu = QtWidgets.QLabel(self)
        self.lbl_goruntu.setGeometry(QtCore.QRect(270, 10, 561, 351))
        self.lbl_goruntu.setStyleSheet("background:#8C85D8;")
        self.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Boyraz_Yolov3_toolkit"))
        self.btn_weight.setText(_translate("self", ".Weight."))
        self.btn_video.setText(" Video")
        self.btn_cfg.setText(_translate("self", "..Cfg.."))
        self.btn_names.setText(_translate("self", ".Names."))
        self.btn_image.setText(_translate("self", " Image "))
        self.btn_imageBasla.setText(_translate("self", "Başla"))
        self.btn_webCamBasla.setText("WebCam")
        self.btn_videoBasla.setText("Başla")


