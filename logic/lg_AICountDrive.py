import json
from PySide6.QtWidgets import QMainWindow, QMessageBox
from interfaces.ui_mainAICountDrive import Ui_MainWindow
from .lg_dashboard import WidgetDashboard
from .lg_camera import WidgetCamera
from .AI.AiCounterDrive import AiCountDrive

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.layoutContainer.addWidget(WidgetDashboard())

        # Events
        self.btnMenu.clicked.connect(self.toggle_left_menu)
        self.btnDashboard.clicked.connect(self.clicked_btn_dashboard)
        self.btnConfiguration.clicked.connect(self.clicked_btn_configuration)
        self.btnCamera.clicked.connect(self.cliked_btn_camera)
        self.btnDestroy.clicked.connect(self.cliked_btn_destroy)

    #Funtions Events
    def clicked_btn_dashboard(self):
        self.lblDashboard.setText("Dashboard")
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetDashboard())

    
    def clicked_btn_configuration(self):
        self.lblDashboard.setText("Configuración")
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetCamera())

    
    def cliked_btn_camera(self):
        self.ai_count_drive = AiCountDrive()
        self.ai_count_drive.destroy_window()
        try:
            with open("camera_auth.json","r") as file:
                data = json.load(file)
                ip = data.get("IP","")
                user = data.get("User","")
                password = data.get("Password","")
            self.ai_count_drive.connect_camera(f'rtsp://{user}:{password}@{ip}/stream')
            self.ai_count_drive.run_count()

        except FileNotFoundError:
            msj = "No hay conexión."
            QMessageBox.critical(self, "Error", msj, QMessageBox.Ok)

    
    def cliked_btn_destroy(self):
        self.ai_count_drive.destroy_window()

    
    def toggle_left_menu(self):
        self.leftMenu.setHidden(not self.leftMenu.isHidden())


    #Funtions Extras
    def destroy_content(self):
        # Eliminar el contenido actual
        while self.layoutContainer.count():
            item = self.layoutContainer.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()