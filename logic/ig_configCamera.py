import json
from PySide6.QtWidgets import QWidget
from interfaces.ui_confiCamera import Ui_ConfiCamera

class ConfigCamera(QWidget,Ui_ConfiCamera):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data()

        self.btnSave.clicked.connect(self.save_data)


    def load_data(self):
        try:
            with open("camera_auth.json","r") as file:
                data = json.load(file)
                self.leIp.setText(data.get("IP",""))
                self.leUser.setText(data.get("User",""))
                self.lePassword.setText(data.get("Password",""))
        except FileNotFoundError:
            pass


    def save_data(self):
        ip = self.leIp.text()
        user = self.leUser.text()
        password = self.lePassword.text()

        data = {"IP":ip,"User":user,"Password":password}

        with open("camera_auth.json","w") as file:
            json.dump(data,file)
        
        print("data save")
        self.close()

