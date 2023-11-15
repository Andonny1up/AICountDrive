# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camerauKFqfN.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(778, 500)
        dashboard.setMinimumSize(QSize(0, 500))
        dashboard.setCursor(QCursor(Qt.ArrowCursor))
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
"}\n"
"QPushButton{\n"
"	background-color: #3838FF;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(dashboard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QWidget(dashboard)
        self.main.setObjectName(u"main")
        self.horizontalLayout_15 = QHBoxLayout(self.main)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frMain = QFrame(self.main)
        self.frMain.setObjectName(u"frMain")
        self.frMain.setFrameShape(QFrame.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frMain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frMain)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 160))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblImg = QLabel(self.frame_3)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setMinimumSize(QSize(80, 80))
        self.lblImg.setMaximumSize(QSize(80, 80))
        self.lblImg.setPixmap(QPixmap(u":/icon-extra/assets/icon-extra/camera-security.png"))
        self.lblImg.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.lblImg, 0, Qt.AlignHCenter)

        self.lblCamera = QLabel(self.frame_3)
        self.lblCamera.setObjectName(u"lblCamera")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblCamera.setFont(font)

        self.verticalLayout_4.addWidget(self.lblCamera, 0, Qt.AlignHCenter)

        self.btnConfiCamera = QPushButton(self.frame_3)
        self.btnConfiCamera.setObjectName(u"btnConfiCamera")
        self.btnConfiCamera.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnConfiCamera)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frMain)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnUpdateVideo = QPushButton(self.frame_2)
        self.btnUpdateVideo.setObjectName(u"btnUpdateVideo")
        self.btnUpdateVideo.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon-white/assets/icon_white/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnUpdateVideo.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btnUpdateVideo, 0, Qt.AlignLeft)

        self.lblVideo = QLabel(self.frame_2)
        self.lblVideo.setObjectName(u"lblVideo")
        self.lblVideo.setMinimumSize(QSize(500, 0))
        self.lblVideo.setMaximumSize(QSize(16777215, 16777215))
        self.lblVideo.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.lblVideo)


        self.horizontalLayout.addWidget(self.frame_2)


        self.horizontalLayout_15.addWidget(self.frMain)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.lblImg.setText("")
        self.lblCamera.setText(QCoreApplication.translate("dashboard", u"Camara", None))
        self.btnConfiCamera.setText(QCoreApplication.translate("dashboard", u"Configurar", None))
        self.btnUpdateVideo.setText(QCoreApplication.translate("dashboard", u"Actualizar", None))
        self.lblVideo.setText("")
    # retranslateUi

