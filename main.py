from PyQt5 import QtWidgets
import sys


from GoruntuIslemeProje.degiskenler.degiskenler import degiskenClass
from GoruntuIslemeProje.fonksiyonlar.DosyaKonumBulma import weightKonumBulma, cfgKonumBulma, namesKonumBulma, imageKonumBulma, videoKonumBulma
from GoruntuIslemeProje.design.tasarim import Ui_Form
from GoruntuIslemeProje.fonksiyonlar.ImageTespit import imageTespiteBasla
from GoruntuIslemeProje.fonksiyonlar.VideoTespit import VideoTespiteBasla
from GoruntuIslemeProje.fonksiyonlar.WebCamTespit import WebCamTespiteBasla

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # NESNE TANIMLAMALARIM
    degiskenler = degiskenClass()
    ui = Ui_Form()

    #TASARIM AYARLAMA


    #-----------------------------------




    #TIKLANMA OLAYLARIM
    ui.btn_weight.clicked.connect(lambda :  weightKonumBulma(degiskenler,ui))
    ui.btn_cfg.clicked.connect(lambda: cfgKonumBulma(degiskenler,ui))
    ui.btn_names.clicked.connect(lambda: namesKonumBulma(degiskenler, ui))

    ui.btn_image.clicked.connect(lambda: imageKonumBulma(degiskenler, ui))
    ui.btn_video.clicked.connect(lambda: videoKonumBulma(degiskenler, ui))

    ui.btn_imageBasla.clicked.connect(lambda: imageTespiteBasla(degiskenler,ui))
    ui.btn_videoBasla.clicked.connect(lambda: VideoTespiteBasla(degiskenler,ui))
    ui.btn_webCamBasla.clicked.connect(lambda: WebCamTespiteBasla(degiskenler,ui))



    sys.exit(app.exec_())

