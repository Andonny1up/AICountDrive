# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAICountDriveYlXPCj.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#leftMenu{\n"
"	background-color: #2a3c3a;\n"
"}\n"
"#topMenu{\n"
"	background-color: #3838FF ;\n"
"}\n"
"#lblNameAplication{\n"
"	color: white;\n"
"}\n"
"#frMenuButtons QPushButton{\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 15px;\n"
"	padding-left:25px;\n"
"}\n"
"#frMenuButtons QPushButton:hover{\n"
"	background-color: #344644;\n"
"}\n"
"#header{\n"
"	background-color: #FDFDFD;\n"
"}\n"
"#header #lblDashboard{\n"
"	color: #3838FF;\n"
"	background-color: white;\n"
"	border-radius: 12px;\n"
"	padding: 5px; \n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(270, 0))
        self.leftMenu.setMaximumSize(QSize(270, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frLeftMenu = QFrame(self.leftMenu)
        self.frLeftMenu.setObjectName(u"frLeftMenu")
        self.frLeftMenu.setFrameShape(QFrame.StyledPanel)
        self.frLeftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frLeftMenu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QWidget(self.frLeftMenu)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 78))
        self.topMenu.setMaximumSize(QSize(16777215, 78))
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, -1, -1, -1)
        self.frTopMenu = QFrame(self.topMenu)
        self.frTopMenu.setObjectName(u"frTopMenu")
        self.frTopMenu.setFrameShape(QFrame.StyledPanel)
        self.frTopMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frTopMenu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblLogo = QLabel(self.frTopMenu)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setMinimumSize(QSize(40, 40))
        self.lblLogo.setMaximumSize(QSize(40, 40))
        self.lblLogo.setPixmap(QPixmap(u":/icon-white/assets/icon_white/cpu.svg"))
        self.lblLogo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lblLogo, 0, Qt.AlignLeft)

        self.lblNameAplication = QLabel(self.frTopMenu)
        self.lblNameAplication.setObjectName(u"lblNameAplication")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.lblNameAplication.setFont(font)
        self.lblNameAplication.setCursor(QCursor(Qt.ArrowCursor))
        self.lblNameAplication.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblNameAplication.setMargin(0)

        self.horizontalLayout_3.addWidget(self.lblNameAplication)


        self.verticalLayout_8.addWidget(self.frTopMenu, 0, Qt.AlignLeft)


        self.verticalLayout_10.addWidget(self.topMenu)

        self.frMenuButtons = QFrame(self.frLeftMenu)
        self.frMenuButtons.setObjectName(u"frMenuButtons")
        self.frMenuButtons.setFrameShape(QFrame.StyledPanel)
        self.frMenuButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frMenuButtons)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btnDashboard = QPushButton(self.frMenuButtons)
        self.btnDashboard.setObjectName(u"btnDashboard")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btnDashboard.setFont(font1)
        self.btnDashboard.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon-white/assets/icon_white/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon)
        self.btnDashboard.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.btnDashboard)

        self.btnCamera = QPushButton(self.frMenuButtons)
        self.btnCamera.setObjectName(u"btnCamera")
        font2 = QFont()
        font2.setPointSize(12)
        self.btnCamera.setFont(font2)
        self.btnCamera.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon-white/assets/icon_white/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCamera.setIcon(icon1)
        self.btnCamera.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.btnCamera)

        self.btnConfiguration = QPushButton(self.frMenuButtons)
        self.btnConfiguration.setObjectName(u"btnConfiguration")
        self.btnConfiguration.setFont(font2)
        self.btnConfiguration.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon-white/assets/icon_white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConfiguration.setIcon(icon2)
        self.btnConfiguration.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.btnConfiguration)


        self.verticalLayout_10.addWidget(self.frMenuButtons, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frLeftMenu)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainContainer)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 0))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuButton = QWidget(self.header)
        self.menuButton.setObjectName(u"menuButton")
        self.horizontalLayout_4 = QHBoxLayout(self.menuButton)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnMenu = QPushButton(self.menuButton)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon-black/assets/icon_black/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon3)
        self.btnMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btnMenu)

        self.lblDashboard = QLabel(self.menuButton)
        self.lblDashboard.setObjectName(u"lblDashboard")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        self.lblDashboard.setFont(font3)

        self.horizontalLayout_4.addWidget(self.lblDashboard)


        self.horizontalLayout_2.addWidget(self.menuButton, 0, Qt.AlignLeft)

        self.UserButton = QWidget(self.header)
        self.UserButton.setObjectName(u"UserButton")
        self.horizontalLayout_5 = QHBoxLayout(self.UserButton)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.UserButton)
        self.pushButton.setObjectName(u"pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon-black/assets/icon_black/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.UserButton, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.layoutContainer = QVBoxLayout()
        self.layoutContainer.setObjectName(u"layoutContainer")

        self.verticalLayout.addLayout(self.layoutContainer)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AICountDrive", None))
        self.lblLogo.setText("")
        self.lblNameAplication.setText(QCoreApplication.translate("MainWindow", u"AICountDrive", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnCamera.setText(QCoreApplication.translate("MainWindow", u"Camara", None))
        self.btnConfiguration.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btnMenu.setText("")
        self.lblDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton.setText("")
    # retranslateUi

