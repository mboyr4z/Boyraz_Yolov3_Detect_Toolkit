import cv2
import numpy as np
from PyQt5 import QtCore,QtGui

def pixmapdonustur(image):      #QLABEL setStyleSheet and setPixmap
    image = QtGui.QImage(image, image.shape[1], \
                         image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(image)
    return pix



def WebCamTespiteBasla(degiskenler,ui):
    if (degiskenler.weightKonum != "" and degiskenler.namesKonum != "" and degiskenler.cfgKonum != ""):
        if (degiskenler.imageKonum != "" or degiskenler.videoKonum != ""):

            net = cv2.dnn.readNet(str(degiskenler.weightKonum), str(degiskenler.cfgKonum))

            classes = []
            # print(degiskenler.weightKonum, degiskenler.cfgKonum,degiskenler.namesKonum,degiskenler.imageKonum,degiskenler.videoKonum)

            with open(str(degiskenler.namesKonum), "r") as f:
                classes = [line.strip() for line in f.readlines()]

            layer_names = net.getLayerNames()

            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            cap = cv2.VideoCapture(0)

            while (cap.isOpened()):
                ret, img = cap.read()  # videodan sürekli resimler al ve ing ye ata
                if ret == True:  # eğer videodan hala resim geliosa yani bitmediyse
                    cv2.waitKey(1)
                    # img = cv2.resize(img, None, fx=0.4, fy=0.4)         #alınmış olan resmi boyutlandır falan filan
                    height, width, channels = img.shape

                    # Detecting objects
                    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                    net.setInput(blob)
                    outs = net.forward(output_layers)

                    # Showing informations on the screen
                    class_ids = []
                    confidences = []
                    boxes = []
                    for out in outs:
                        for detection in out:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]

                            if confidence > 0.5:
                                # Object detected
                                center_x = int(detection[0] * width)
                                center_y = int(detection[1] * height)
                                w = int(detection[2] * width)
                                h = int(detection[3] * height)

                                # Rectangle coordinates
                                x = int(center_x - w / 2)
                                y = int(center_y - h / 2)

                                boxes.append([x, y, w, h])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)

                    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                    font = cv2.FONT_HERSHEY_PLAIN
                    for i in range(len(boxes)):
                        if i in indexes:
                            x, y, w, h = boxes[i]
                            label = str(classes[class_ids[i]])
                            color = colors[class_ids[i]]
                            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

                    img = cv2.resize(img, (561, 351))

                    pixmap = pixmapdonustur(img)

                    ui.lbl_goruntu.setPixmap(pixmap)