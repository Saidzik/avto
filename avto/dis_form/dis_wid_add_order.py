# Form implementation generated from reading ui file 'dis_wid_order.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_order(object):
    def setupUi(self, Dialog_order):
        Dialog_order.setObjectName("Dialog_order")
        Dialog_order.resize(392, 249)
        Dialog_order.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.539773 rgba(14, 23, 106, 255), stop:1 rgba(85, 170, 255, 255));\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_order)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Dialog_order)
        self.frame.setStyleSheet("background-color: rgba(255, 255 ,255 ,30 );\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 10px;")
        self.frame.setObjectName("frame")
        self.layout_param = QtWidgets.QVBoxLayout(self.frame)
        self.layout_param.setObjectName("layout_param")
        self.cb_clients = QtWidgets.QComboBox(parent=self.frame)
        self.cb_clients.setMaximumSize(QtCore.QSize(3203402, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        self.cb_clients.setFont(font)
        self.cb_clients.setStyleSheet("border-radius: 5px;\n"
"\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"width:230px;\n"
"height:40px;")
        self.cb_clients.setCurrentText("")
        self.cb_clients.setObjectName("cb_clients")
        self.layout_param.addWidget(self.cb_clients)
        self.cb_pay = QtWidgets.QComboBox(parent=self.frame)
        self.cb_pay.setMaximumSize(QtCore.QSize(3203402, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        self.cb_pay.setFont(font)
        self.cb_pay.setStyleSheet("border-radius: 5px;\n"
"\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"width:230px;\n"
"height:40px;")
        self.cb_pay.setObjectName("cb_pay")
        self.layout_param.addWidget(self.cb_pay)
        self.le_price = QtWidgets.QLineEdit(parent=self.frame)
        self.le_price.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        self.le_price.setFont(font)
        self.le_price.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border: 1px solid gray;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius: 10px;\n"
"width:230px;\n"
"height:40px;")
        self.le_price.setObjectName("le_price")
        self.layout_param.addWidget(self.le_price)
        self.verticalLayout_2.addWidget(self.frame)
        self.but_save_add = QtWidgets.QPushButton(parent=Dialog_order)
        self.but_save_add.setEnabled(True)
        self.but_save_add.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.but_save_add.setFont(font)
        self.but_save_add.setStyleSheet("QPushButton{\n"
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
        self.but_save_add.setIcon(icon)
        self.but_save_add.setIconSize(QtCore.QSize(30, 30))
        self.but_save_add.setObjectName("but_save_add")
        self.verticalLayout_2.addWidget(self.but_save_add)

        self.retranslateUi(Dialog_order)
        self.cb_clients.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_order)

    def retranslateUi(self, Dialog_order):
        _translate = QtCore.QCoreApplication.translate
        Dialog_order.setWindowTitle(_translate("Dialog_order", "Dialog"))
        self.le_price.setPlaceholderText(_translate("Dialog_order", "Цена"))
        self.but_save_add.setText(_translate("Dialog_order", "🤝Оформировать"))
