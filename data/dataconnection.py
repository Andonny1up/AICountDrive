import os
from PySide6.QtSql import QSqlDatabase, QSqlQuery

class DataConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = None
        self.query = QSqlQuery()

    def check_database(self):
        if not os.path.exists(self.db_name):
            self.create_database()

    def create_database(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_name)
        if not self.db.open():
            raise Exception("Error al crear la base de datos")


        # Aquí se creara una tabla llamada 'VEHICLES' con id y type
        query = QSqlQuery()
        # verificar si la tabla 'vehicles' existe
        query.exec_("select * from vehicles")
        if not query.next():
            # si no existe, se crea la tabla
            query.exec_("""create table vehicles(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type varchar(20),
                        date datetime default current_timestamp
                        )""")
        
        #insertar datos de prueba
        query.exec_("insert into vehicles (type) values('auto')")
        query.exec_("insert into vehicles (type) values('camion')")
        query.exec_("insert into vehicles (type) values('moto')")
        query.exec_("insert into vehicles (type) values('moto')")
        #ahora hay que mandar estas modificaciones a la base de datos
        self.db.commit()

        self.db.close()

    def open_connection(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_name)
        if not self.db.open():
            raise Exception("Error al abrir la conexión")

    def close_connection(self):
        if self.db:
            self.db.close()


# Ejemplo de uso
# db_name = "/C:/Users/User/Projects/AICountDrive/data/mydatabase.db"
# data_connection = DataConnection(db_name)
# data_connection.check_database()
# data_connection.open_connection()

# Realiza operaciones en la base de datos

# data_connection.close_connection()
