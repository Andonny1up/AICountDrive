# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confiCameraxvnPGS.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ConfiCamera(object):
    def setupUi(self, ConfiCamera):
        if not ConfiCamera.objectName():
            ConfiCamera.setObjectName(u"ConfiCamera")
        ConfiCamera.resize(250, 235)
        ConfiCamera.setMinimumSize(QSize(250, 235))
        ConfiCamera.setMaximumSize(QSize(250, 235))
        ConfiCamera.setStyleSheet(u"#ConfiCamera{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#frmContainer{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #3838FF;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(ConfiCamera)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmContainer = QFrame(ConfiCamera)
        self.frmContainer.setObjectName(u"frmContainer")
        self.frmContainer.setFrameShape(QFrame.StyledPanel)
        self.frmContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frmContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frmContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblIP = QLabel(self.frame_2)
        self.lblIP.setObjectName(u"lblIP")

        self.verticalLayout_2.addWidget(self.lblIP)

        self.leIp = QLineEdit(self.frame_2)
        self.leIp.setObjectName(u"leIp")

        self.verticalLayout_2.addWidget(self.leIp)

        self.lblUser = QLabel(self.frame_2)
        self.lblUser.setObjectName(u"lblUser")

        self.verticalLayout_2.addWidget(self.lblUser)

        self.leUser = QLineEdit(self.frame_2)
        self.leUser.setObjectName(u"leUser")

        self.verticalLayout_2.addWidget(self.leUser)

        self.lblPassword = QLabel(self.frame_2)
        self.lblPassword.setObjectName(u"lblPassword")

        self.verticalLayout_2.addWidget(self.lblPassword)

        self.lePassword = QLineEdit(self.frame_2)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.lePassword)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frmContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSave = QPushButton(self.frame_3)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frmContainer)


        self.retranslateUi(ConfiCamera)

        QMetaObject.connectSlotsByName(ConfiCamera)
    # setupUi

    def retranslateUi(self, ConfiCamera):
        ConfiCamera.setWindowTitle(QCoreApplication.translate("ConfiCamera", u"Configurar Camara", None))
        self.lblIP.setText(QCoreApplication.translate("ConfiCamera", u"IP:", None))
        self.lblUser.setText(QCoreApplication.translate("ConfiCamera", u"Usuario:", None))
        self.lblPassword.setText(QCoreApplication.translate("ConfiCamera", u"Contrase\u00f1a:", None))
        self.btnSave.setText(QCoreApplication.translate("ConfiCamera", u"Guardar", None))
    # retranslateUi

