from PySide6.QtWidgets import QMainWindow
from interfaces.ui_mainAICountDrive import Ui_MainWindow
from .lg_dashboard import WidgetDashboard
from .lg_camera import WidgetCamera

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.layoutContainer.addWidget(WidgetDashboard())

        # Events
        self.btnMenu.clicked.connect(self.toggle_left_menu)
        self.btnDashboard.clicked.connect(self.clicked_btn_dashboard)
        self.btnCamera.clicked.connect(self.clicked_btn_camera)

    #Funtions Events
    def clicked_btn_dashboard(self):
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetDashboard())

    
    def clicked_btn_camera(self):
        self.destroy_content()
        self.layoutContainer.addWidget(WidgetCamera())

    
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