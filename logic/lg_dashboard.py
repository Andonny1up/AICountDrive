from PySide6.QtWidgets import QWidget
from interfaces.ui_dashboard import Ui_dashboard
from data.dataconnection import DataConnection
from helpers import absPath

class WidgetDashboard(QWidget,Ui_dashboard):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.database_create_connection()
        self.count_vehicles()

    #necesito una funcion que me permita conectar a la base de datos y traer datos de la tablla vehicles
    # CONTARA los vehiculos segun su tipo y segun el mes actual

    def database_create_connection(self):
        db_name = absPath("data/AiCountDrive.db")
        self.data_connection = DataConnection(db_name)
        self.data_connection.check_database()
        self.data_connection.close_connection()

    
    def count_vehicles(self):
        #contar autos
        self.data_connection.open_connection()
        query = self.data_connection.db.exec_("select count(*) from vehicles where type = 'auto'")
        query.next()
        count = query.value(0)
        self.lblCarCount.setText(str(count))
        self.data_connection.close_connection()

        #contar motos
        self.data_connection.open_connection()
        query = self.data_connection.db.exec_("select count(*) from vehicles where type = 'moto'")
        query.next()
        count = query.value(0)
        self.lblMotoCount.setText(str(count))
        self.data_connection.close_connection()

        #contar camiones
        self.data_connection.open_connection()
        query = self.data_connection.db.exec_("select count(*) from vehicles where type = 'camion'")
        query.next()
        count = query.value(0)
        self.lblCamionCount.setText(str(count))
        self.data_connection.close_connection()

        # contar buses
        self.data_connection.open_connection()
        query = self.data_connection.db.exec_("select count(*) from vehicles where type = 'bus'")
        query.next()
        count = query.value(0)
        self.lblBusCount.setText(str(count))
        self.data_connection.close_connection()
