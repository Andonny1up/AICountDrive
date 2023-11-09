import cv2 as cv
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget
from interfaces.ui_camera import Ui_dashboard

class WidgetCamera(QWidget,Ui_dashboard):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #captura video
        self.cap = cv.VideoCapture("rtsp://admin:12345@192.168.14.251/stream")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_video)
        self.timer.start(30)


    def show_video(self):
        ret, frame = self.cap.read()
        
        if ret:
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data,width,height,bytes_per_line,QImage.Format.Format_RGB888).rgbSwapped()

            pixmap = QPixmap.fromImage(q_img)
            self.lblVideo.setPixmap(pixmap)