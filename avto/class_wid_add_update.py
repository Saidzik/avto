
from PyQt6.QtWidgets import QFileDialog, QPushButton, QLineEdit, QMessageBox, QDateEdit, QDialog, QComboBox, QMenuBar, QMenu, QTableWidgetItem, QTableView, QHeaderView, QVBoxLayout, QLabel
from PyQt6.QtCore import QDateTime, Qt, QDate, QEvent
import shutil
from datetime import date, datetime
from dis_form.dis_wid_add_update import Ui_Dialog_add
from class_database import Database
from random import randint

import os



class widget_add(QDialog, Ui_Dialog_add):
    def __init__(self, table_name, function_name, position, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)  # Устанавливаем модальное окно
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        self.datab = Database()  # Подключение к базе данных
        self.main = MainWindow  # Главное окно
        self.table_name = table_name  # Имя таблицы
        self.function_name = function_name
        self.position = position
        self.data_photo = []

        self.creating_widget_add_fields()  # Создаем поля для добавления данных

    def creating_widget_add_fields(self):
        try:
            self.clear_layout()  # Очищаем старые поля
            columns =  self.datab.get_holder(self.table_name)
            print(columns)
            columns.remove('ID')

            for column in columns:
                if 'ID_' in column:
                    fields = QComboBox()  # Для колонок с ID создаем ComboBox
                    self.add_item_comboBox(fields, column)
                elif 'Дата' in column:
                    fields = QDateEdit()  # Для колонок с датой создаем DateEdit
                elif 'Фото' in column:
                    fields = QPushButton()
                    fields.setText('NULL')
                    fields.clicked.connect(self.select_file)

                elif 'Статус' in column:
                    fields = QComboBox()  # Для колонок с ID создаем ComboBox
                    fields.addItem('Активный')
                    fields.addItem('Уволен')
                    if self.position == 'Сотрудник' or self.table_name == 'Автомобили':
                        fields.setEnabled(False)


                elif 'Должность' in column:
                    fields = QComboBox()  # Для колонок с ID создаем ComboBox
                    fields.addItem('Руководитель')
                    fields.addItem('Сотрудник')
                    if self.position == 'Сотрудник':
                        fields.setEnabled(False)
                else:
                    fields = QLineEdit()  # Для остальных колонок создаем текстовое поле
                    fields.setPlaceholderText(column)  # Устанавливаем текст-подсказку


                self.stile_fields(fields)  # Применяем стили к полям
                self.layout_param.addWidget(fields)  # Добавляем поля в макет


        except Exception as e:
            QMessageBox.information(self, 'Внимание', 'Заполните поле для поиска!')
            print(f"7 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        forbidden_folder = "/photo"

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]  # Получаем путь к выбранному файлу

            if forbidden_folder in selected_file:
                QMessageBox.warning(None, "Ошибка", "Доступ к этой папке запрещен!")
                return

            destination_folder = "photo"

            file_name = os.path.basename(selected_file)
            destination_path = os.path.join(destination_folder, file_name)

            self.data_photo = [selected_file, destination_path]

    def move_file(self, selected_file, destination_path):
        try:
                # Перемещаем файл в целевую папку
            shutil.copy(selected_file, destination_path)
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'Не удалось: {str(e)}')

    def clear_layout(self):
        try:
            while self.layout_param.count():
                item = self.layout_param.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        except Exception as e:
            print(f"8 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def add_item_comboBox(self, fields, column):
        try:
            table_name = column.replace("ID_", "")  # Убираем префикс ID_
            for item in self.datab.query_fields_for_comboBox(table_name):  # Получаем данные для ComboBox
                fields.addItem(item)


        except Exception as e:
            print(f"9 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def opr_widget_add_fields(self):
        try:
            widget_add_fields = []
            for i in range(self.layout_param.count()):
                item = self.layout_param.itemAt(i)
                if item.widget():
                    widget_add_fields.append(item.widget())  # Добавляем виджет в список
            return widget_add_fields


        except Exception as e:
            print(f"10 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def open_widget_add(self, id):
        try:
            widget_add_fields = self.opr_widget_add_fields()  # Получаем виджеты полей ввода
            if self.function_name == '🖋️ Изменить':
                if id:
                    data_of_table = self.datab.query_select_table_by_id(self.table_name, id)[0]  # Получаем данные по ID
                    self.output_of_fields(data_of_table, widget_add_fields)  # Заполняем поля данными
                    self.but_save_add.clicked.connect(lambda: self.update_column(id, widget_add_fields))  # Подключаем кнопку сохранения
                    self.show()
                else:
                    QMessageBox.information(self, 'Внимание', 'Выберите ID')

            elif self.function_name == '➕ Новый':
                self.but_save_add.clicked.connect(lambda: self.add_new_column(widget_add_fields))  # Подключаем кнопку добавления
                self.show()

            elif self.function_name == '🚛':
                return widget_add_fields





        except Exception as e:
            print(f"11 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def create_delivers(self, widget_add_fields):
        try:
            table_name = 'deliveries'
            id = self.datab.incr(table_name)
            values = self.opr_of_field_values(id, widget_add_fields)

            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            values.append(formatted_datetime)
            values.append(0)
            self.datab.query_add_new_column(table_name, values)  # Добавляем новую запись
            self.close()
            return values

        except Exception as e:
            print(f"12 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def create_sales(self):
        try:
            table_name = 'sales'
            id = self.datab.incr(table_name)
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            values = [id, formatted_datetime, 0]
            self.datab.query_add_new_column(table_name, values)  # Добавляем новую запись
            self.close()
            return values

        except Exception as e:
            print(f"13 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def add_new_column(self, widget_add_fields):
        try:
            id = self.datab.incr(self.table_name)  # Получаем новый ID
            values = self.opr_of_field_values(id, widget_add_fields)  # Получаем значения полей
            print(values)
            if values:
                self.datab.query_add_new_column(self.table_name, values)  # Добавляем новую запись
                self.data_photo.clear()
                self.close()
                self.main.opr_sql_query()

        except Exception as e:
            print(f"14 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def opr_of_field_values(self, id, widget_add_fields):
        try:
            values = []
            values.append(id)  # Добавляем ID
            value = None
            for field in widget_add_fields:  # Обрабатываем каждое поле

                if isinstance(field, QComboBox):
                    value_name = field.currentText() if field.currentIndex() != -1 else field.placeholderText()
                    columns =  self.datab.get_holder(self.table_name)
                    print(field.placeholderText())
                    if value_name in ['Активный', 'Уволен','Руководитель','Сотрудник']:
                        value = value_name
                    else:
                        for column in columns:
                            if 'ID_' in column:
                                table_name = column.replace("ID_", "")
                                value = self.datab.query_opr_id(table_name, value_name)
                                if value:
                                    break


                elif isinstance(field, QDateEdit):
                    date = field.date()
                    value = date.toString(Qt.DateFormat.ISODate)  # Форматируем дату

                elif isinstance(field, QPushButton):
                    if self.data_photo != []:
                        value = self.data_photo[1]
                        self.move_file(self.data_photo[0], self.data_photo[1])
                        if os.path.exists(field.text()) and 'photo/' not in field.text():
                            os.remove(field.text())

                    else:
                        value = field.text()
                else:
                    value = str(field.text()).strip()
                    column = field.placeholderText()
                    int_columns = self.datab.get_integer_columns(self.table_name)
                    dec_columns = self.datab.get_decimal_columns(self.table_name)

                    if column in ['Пароль', 'Логин'] and len(value) < 6:
                        value = str(randint(100000, 999999))
                    # Проверка и преобразование для целых чисел
                    if column in int_columns:
                        try:
                            value = int(value)
                        except ValueError:
                            print(f"Значение '{value}' не является целым числом.")
                            field.setText('')
                            field.setPlaceholderText('Неправильные данные!')
                            return False

                    # Проверка и преобразование для чисел с плавающей точкой
                    elif column in dec_columns:
                        try:
                            value = float(value)
                        except ValueError:
                            print(f"Значение '{value}' не является числом с плавающей точкой.")
                            field.setText('')
                            field.setPlaceholderText('Неправильные данные!')
                            return False

                values.append(value)
            return values  # Возвращаем список значений

        except Exception as e:
            print(f"15 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def is_float(self, value) :
        try:
            float(value)
            return True
        except ValueError:
            return False

    def update_column(self, id, widget_add_fields):
        try:
            values = self.opr_of_field_values(id, widget_add_fields)
            print('sfdfv',values)
            print(values)
            if values:
                holders = [holder.strip() for holder in self.datab.get_holder(self.table_name)]
                print(1)# Получаем названия колонок
                self.datab.query_update_column(holders, values, self.table_name)  # Выполняем запрос на обновление
                self.close()
                self.main.opr_sql_query()  # Обновляем таблицу

        except Exception as e:
            print(f"16 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def output_of_fields(self, data, widget_add_fields):
        try:
            for i, le in enumerate(widget_add_fields, start=1):
                value = data[i] if data[i] is not None else ""  # Получаем значение для каждого поля
                if isinstance(le, QComboBox):

                    if value in ['Руководитель','Сотрудник','Уволен','Активный']:
                        le.setCurrentText(value)
                    elif value == "":
                        le.setCurrentIndex(0)
                    else:
                        le.setCurrentIndex(int(value)-1)

                elif isinstance(le, QDateEdit):
                    date = QDate.fromString(str(value), "yyyy-MM-dd")  # Преобразуем строку в дату
                    le.setDate(date)
                elif isinstance(le, QPushButton):
                    le.setText(str(value.replace("\\", "/")))
                else:
                    le.setText(str(value))  # Преобразуем значение в строку и устанавливаем текст в поле

        except Exception as e:
            print(f"17 Ошибка при выполнении запроса: {e}")  # Обработка ошибок

    def stile_fields(self, fields):
        fields.setStyleSheet("\n"
                             "border-radius: 7px;\n"
                             "width:230px;\n"
                             "height:35px")