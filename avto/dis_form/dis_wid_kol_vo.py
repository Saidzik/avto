# Form implementation generated from reading ui file 'dis_wid_kol_vo.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_kol_vo(object):
    def setupUi(self, Dialog_kol_vo):
        Dialog_kol_vo.setObjectName("Dialog_kol_vo")
        Dialog_kol_vo.resize(336, 132)
        Dialog_kol_vo.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.539773 rgba(14, 23, 106, 255), stop:1 rgba(85, 170, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_kol_vo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Dialog_kol_vo)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_kol = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        self.le_kol.setFont(font)
        self.le_kol.setStyleSheet("border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"color: rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"width:230px;\n"
"height:40px;")
        self.le_kol.setObjectName("le_kol")
        self.verticalLayout.addWidget(self.le_kol)
        self.but_confirm = QtWidgets.QPushButton(parent=self.frame)
        self.but_confirm.setEnabled(True)
        self.but_confirm.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.but_confirm.setFont(font)
        self.but_confirm.setStyleSheet("QPushButton{\n"
"background-color: rgba(255,255,255,30);\n"
"color: rgba(255, 255, 255, 255);\n"
"border-radius: 10px;\n"
"width:230px;\n"
"height:40px;}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,30);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res-add/icons/post_add_white_24dp.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.but_confirm.setIcon(icon)
        self.but_confirm.setIconSize(QtCore.QSize(30, 30))
        self.but_confirm.setObjectName("but_confirm")
        self.verticalLayout.addWidget(self.but_confirm)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog_kol_vo)
        QtCore.QMetaObject.connectSlotsByName(Dialog_kol_vo)

    def retranslateUi(self, Dialog_kol_vo):
        _translate = QtCore.QCoreApplication.translate
        Dialog_kol_vo.setWindowTitle(_translate("Dialog_kol_vo", "Dialog"))
        self.le_kol.setPlaceholderText(_translate("Dialog_kol_vo", "Количество"))
        self.but_confirm.setText(_translate("Dialog_kol_vo", "Потвердить"))
