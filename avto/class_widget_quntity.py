from PyQt6.QtWidgets import QFileDialog,QApplication, QMainWindow, QTableView, QWidget, QPushButton, QLineEdit, QMessageBox, QDateEdit, QDialog, QComboBox, QMenuBar, QMenu, QTableWidgetItem, QTableView, QHeaderView, QVBoxLayout, QLabel
from PyQt6.QtCore import QDateTime, Qt, QDate, QEvent
from dis_form.dis_wid_kol_vo import Ui_Dialog_kol_vo









class widget_add_kol_vo(QDialog, Ui_Dialog_kol_vo):
    def __init__(self, table_name, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        #self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)