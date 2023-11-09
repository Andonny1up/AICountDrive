from PySide6.QtWidgets import QWidget
from interfaces.ui_dashboard import Ui_dashboard

class WidgetDashboard(QWidget,Ui_dashboard):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)