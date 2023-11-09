# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardgHMFvK.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(703, 500)
        dashboard.setMinimumSize(QSize(0, 500))
        dashboard.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"#dashboard{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#cards QFrame{\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"#frMain{\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.verticalLayout = QVBoxLayout(dashboard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cards = QWidget(dashboard)
        self.cards.setObjectName(u"cards")
        self.cards.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_6 = QHBoxLayout(self.cards)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.card1 = QFrame(self.cards)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frCount1 = QFrame(self.card1)
        self.frCount1.setObjectName(u"frCount1")
        self.frCount1.setFrameShape(QFrame.StyledPanel)
        self.frCount1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frCount1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblMotoCount = QLabel(self.frCount1)
        self.lblMotoCount.setObjectName(u"lblMotoCount")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.lblMotoCount.setFont(font)

        self.horizontalLayout_7.addWidget(self.lblMotoCount)

        self.lblIconMoto = QLabel(self.frCount1)
        self.lblIconMoto.setObjectName(u"lblIconMoto")
        self.lblIconMoto.setMinimumSize(QSize(65, 65))
        self.lblIconMoto.setMaximumSize(QSize(65, 65))
        self.lblIconMoto.setPixmap(QPixmap(u":/icon-v/assets/icon_vehicles/moto.png"))
        self.lblIconMoto.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lblIconMoto)


        self.verticalLayout_3.addWidget(self.frCount1)

        self.frLbl1 = QFrame(self.card1)
        self.frLbl1.setObjectName(u"frLbl1")
        self.frLbl1.setFrameShape(QFrame.StyledPanel)
        self.frLbl1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frLbl1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblMotos = QLabel(self.frLbl1)
        self.lblMotos.setObjectName(u"lblMotos")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblMotos.setFont(font1)

        self.horizontalLayout_11.addWidget(self.lblMotos)


        self.verticalLayout_3.addWidget(self.frLbl1)


        self.horizontalLayout_6.addWidget(self.card1)

        self.card2 = QFrame(self.cards)
        self.card2.setObjectName(u"card2")
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frCount2 = QFrame(self.card2)
        self.frCount2.setObjectName(u"frCount2")
        self.frCount2.setFrameShape(QFrame.StyledPanel)
        self.frCount2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frCount2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblCarCount = QLabel(self.frCount2)
        self.lblCarCount.setObjectName(u"lblCarCount")
        self.lblCarCount.setFont(font)

        self.horizontalLayout_8.addWidget(self.lblCarCount)

        self.lblIconCar = QLabel(self.frCount2)
        self.lblIconCar.setObjectName(u"lblIconCar")
        self.lblIconCar.setMinimumSize(QSize(65, 65))
        self.lblIconCar.setMaximumSize(QSize(65, 65))
        self.lblIconCar.setPixmap(QPixmap(u":/icon-v/assets/icon_vehicles/coche.png"))
        self.lblIconCar.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.lblIconCar)


        self.verticalLayout_4.addWidget(self.frCount2)

        self.frLbl2 = QFrame(self.card2)
        self.frLbl2.setObjectName(u"frLbl2")
        self.frLbl2.setFrameShape(QFrame.StyledPanel)
        self.frLbl2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frLbl2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lblCar = QLabel(self.frLbl2)
        self.lblCar.setObjectName(u"lblCar")
        self.lblCar.setFont(font1)

        self.horizontalLayout_12.addWidget(self.lblCar)


        self.verticalLayout_4.addWidget(self.frLbl2)


        self.horizontalLayout_6.addWidget(self.card2)

        self.card3 = QFrame(self.cards)
        self.card3.setObjectName(u"card3")
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frCount3 = QFrame(self.card3)
        self.frCount3.setObjectName(u"frCount3")
        self.frCount3.setFrameShape(QFrame.StyledPanel)
        self.frCount3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frCount3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblBusCount = QLabel(self.frCount3)
        self.lblBusCount.setObjectName(u"lblBusCount")
        self.lblBusCount.setFont(font)

        self.horizontalLayout_9.addWidget(self.lblBusCount)

        self.lblIconBus = QLabel(self.frCount3)
        self.lblIconBus.setObjectName(u"lblIconBus")
        self.lblIconBus.setMinimumSize(QSize(65, 65))
        self.lblIconBus.setMaximumSize(QSize(65, 65))
        self.lblIconBus.setPixmap(QPixmap(u":/icon-v/assets/icon_vehicles/autobus.png"))
        self.lblIconBus.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.lblIconBus)


        self.verticalLayout_5.addWidget(self.frCount3)

        self.frLbl3 = QFrame(self.card3)
        self.frLbl3.setObjectName(u"frLbl3")
        self.frLbl3.setFrameShape(QFrame.StyledPanel)
        self.frLbl3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frLbl3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblBuses = QLabel(self.frLbl3)
        self.lblBuses.setObjectName(u"lblBuses")
        self.lblBuses.setFont(font1)

        self.horizontalLayout_13.addWidget(self.lblBuses)


        self.verticalLayout_5.addWidget(self.frLbl3)


        self.horizontalLayout_6.addWidget(self.card3)

        self.card4 = QFrame(self.cards)
        self.card4.setObjectName(u"card4")
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.card4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frCount4 = QFrame(self.card4)
        self.frCount4.setObjectName(u"frCount4")
        self.frCount4.setFrameShape(QFrame.StyledPanel)
        self.frCount4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frCount4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblCamionCount = QLabel(self.frCount4)
        self.lblCamionCount.setObjectName(u"lblCamionCount")
        self.lblCamionCount.setFont(font)

        self.horizontalLayout_10.addWidget(self.lblCamionCount)

        self.lblIconCamion = QLabel(self.frCount4)
        self.lblIconCamion.setObjectName(u"lblIconCamion")
        self.lblIconCamion.setMinimumSize(QSize(65, 65))
        self.lblIconCamion.setMaximumSize(QSize(65, 65))
        self.lblIconCamion.setPixmap(QPixmap(u":/icon-v/assets/icon_vehicles/camion.png"))
        self.lblIconCamion.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.lblIconCamion)


        self.verticalLayout_6.addWidget(self.frCount4)

        self.frLbl4 = QFrame(self.card4)
        self.frLbl4.setObjectName(u"frLbl4")
        self.frLbl4.setFrameShape(QFrame.StyledPanel)
        self.frLbl4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frLbl4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lblCamion = QLabel(self.frLbl4)
        self.lblCamion.setObjectName(u"lblCamion")
        self.lblCamion.setFont(font1)

        self.horizontalLayout_14.addWidget(self.lblCamion)


        self.verticalLayout_6.addWidget(self.frLbl4)


        self.horizontalLayout_6.addWidget(self.card4)


        self.verticalLayout.addWidget(self.cards)

        self.main = QWidget(dashboard)
        self.main.setObjectName(u"main")
        self.horizontalLayout_15 = QHBoxLayout(self.main)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frMain = QFrame(self.main)
        self.frMain.setObjectName(u"frMain")
        self.frMain.setFrameShape(QFrame.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frMain)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.lblMotoCount.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.lblIconMoto.setText("")
        self.lblMotos.setText(QCoreApplication.translate("dashboard", u"Motos", None))
        self.lblCarCount.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.lblIconCar.setText("")
        self.lblCar.setText(QCoreApplication.translate("dashboard", u"Autos", None))
        self.lblBusCount.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.lblIconBus.setText("")
        self.lblBuses.setText(QCoreApplication.translate("dashboard", u"Buses", None))
        self.lblCamionCount.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.lblIconCamion.setText("")
        self.lblCamion.setText(QCoreApplication.translate("dashboard", u"Camiones", None))
    # retranslateUi

