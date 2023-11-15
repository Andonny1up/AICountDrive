import cv2 as cv
import json
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget
from interfaces.ui_camera import Ui_dashboard
from .ig_configCamera import ConfigCamera

class WidgetCamera(QWidget,Ui_dashboard):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.subwindow_confi_camera = ConfigCamera()
        self.btnConfiCamera.clicked.connect(self.show_subwindow_confi)
        self.btnUpdateVideo.clicked.connect(self.cliked_btnUpdateVideo)

        #captura video
        self.connect_camera()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_video)
        self.timer.start(30)


    def connect_camera(self):
        try:
            with open("camera_auth.json","r") as file:
                data = json.load(file)
                ip = data.get("IP","")
                user = data.get("User","")
                password = data.get("Password","")
            
            self.cap = cv.VideoCapture(f'rtsp://{user}:{password}@{ip}/stream')

        except FileNotFoundError:
            pass
    
    #events
    def cliked_btnUpdateVideo(self):
        self.connect_camera()


    def show_subwindow_confi(self):
        self.subwindow_confi_camera = ConfigCamera()
        self.subwindow_confi_camera.show()


    def show_video(self):
        ret, frame = self.cap.read()
        
        if ret:
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data,width,height,bytes_per_line,QImage.Format.Format_RGB888).rgbSwapped()

            pixmap = QPixmap.fromImage(q_img)
            self.lblVideo.setPixmap(pixmap)
        else:
            self.lblVideo.setText("Sin conexion")