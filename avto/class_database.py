import sqlite3
from statistics import quantiles


class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.create_connection()


    def create_connection(self):
        self.db = sqlite3.connect('db_avto.db')
        self.cursor = self.db.cursor()


    def execute_query_with_params(self, sql_query, values_query=None):
        try:
            if values_query is not None:
                self.cursor.execute(sql_query, values_query)
            else:
                self.cursor.execute(sql_query)

        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def get_data_table_with_date(self, view_name, date_start, date_end):

        # Подготовка SQL-запроса с параметризованными значениями для защиты от SQL-инъекций
        if  view_name == 'Продажи сотрудников за период':
            sql_query = f"""SELECT 
                                        ID_Сотрудника, 
                                        Сотрудник, 
                                        Должность, 
                                        Количество_Продаж, 
                                        Общая_Выручка
                                    FROM {view_name}
                                    WHERE Дата_продажи BETWEEN '{date_start}' AND '{date_end}';"""
        else:
            sql_query = f"SELECT * FROM {view_name} WHERE Дата_продажи BETWEEN '{date_start}' AND '{date_end}';"
        # Выполнение запроса с передачей параметров
        self.cursor.execute(sql_query)
        # Извлечение данных
        data = self.cursor.fetchall()
        columns = [description[0] for description in self.cursor.description]
        return data, columns


    def query_entry(self, login, password, position):
        self.execute_query_with_params(f'''SELECT ID, Логин, Пароль, Должность FROM Сотрудники where Логин = ? and Пароль = ? and Должность=? and Статус = 'Активный' ''', [login, password, position])
        data = self.cursor.fetchone()
        return data

    def get_price(self, table_name, id):
        self.cursor.execute(f'SELECT Цена FROM {table_name} WHERE ID={id}')
        data = self.cursor.fetchone()[0]
        print(data)
        return data

    def query_exists_id(self, table_name, record_id):
        try:
            # Используем параметризованный запрос для защиты от SQL-инъекций
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (int(record_id),))
            data = self.cursor.fetchall()

            # Отладочная информация
            print("Результат запроса:", data)

            return bool(data)  # Преобразуем в True, если данные есть, иначе False
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return False

    def update_total_amount(self, table_name, total_amount, id_sales_delivers):

        query = f'''UPDATE {table_name} SET total_amount = ? WHERE id = ?'''
        self.cursor.execute(query, (total_amount, id_sales_delivers))
        self.db.commit()

    def query_sum_orders(self, table_name, column, id_sales_delivers):
        query = f'''
            SELECT SUM(CAST(quantity AS REAL) / unit.minimum_unit * sweets.price) FROM {table_name}
            JOIN sweets on sweets_id = sweets.id 
            JOIN unit on sweets.unit_id = unit.id WHERE {column} = ? ;
        '''
        self.cursor.execute(query, (id_sales_delivers,))
        sum_order = self.cursor.fetchone()[0]
        if sum_order:
            sum_order = float(sum_order)
            result = round(sum_order, 3)
        else:
            result = 0

        return result

    def query_table(self, table_name, id):
        if table_name == 'EMPLOYEE':
            self.cursor.execute(f'''SELECT EMPLOYEE.ID, FIRST_NAME, LAST_NAME, MIDDLE_NAME, PCK.NAME, PHONE_NUMBER, BIRTHDATE, POSIT, EMAIL
            FROM employee JOIN pck on employee.id_pck = pck.id WHERE employee.id = {id}''')
        else:
            self.cursor.execute(f'SELECT * FROM {table_name} WHERE ID={id}')
        data = self.cursor.fetchall()[0]
        return data

    def query_add_sweets_of_sales_delivers(self, sweets_id, id_sales_delivers, quantity, table_name):
        try:

            self.cursor.execute('SELECT sweets.remains FROM sweets WHERE id = ?', [sweets_id])
            sweet_kol = int(self.cursor.fetchone()[0])
            id_item = self.incr(table_name)
            param = [id_item, id_sales_delivers, sweets_id, quantity ]

            if table_name == 'delivery_items' :
                self.cursor.execute(f'INSERT INTO {table_name} VALUES{tuple(param)};')
                self.db.commit()
                return True

            elif sweet_kol >= int(quantity) and table_name == 'sale_items' :
                self.cursor.execute(f'INSERT INTO {table_name} VALUES{tuple(param)};')
                self.db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Ошибка при добавлении товара в продажу: {e}")
            return False

    def query_repeat_check(self, sweets_id, id_sales_delivers, table_name, column):
        try:
            # Выполнение параметризованного SQL-запроса
            query = f'SELECT COUNT(id) FROM {table_name} WHERE {column} = ? AND sweets_id = ?'
            self.cursor.execute(query, (id_sales_delivers, sweets_id))

            row_count = int(self.cursor.fetchone()[0])

            # Возвращаем True, если строк нет, иначе False
            return row_count == 0
        except Exception as e:
            print(f"Ошибка при проверке записи в таблице {table_name}: {e}")
            return False

    def query_select_table_by_id(self, table_name, id):
        self.cursor.execute(f'SELECT * FROM {table_name} WHERE ID={id}')
        data = self.cursor.fetchall()
        return data

    def query_opr_min_unit(self, id):
        # Выполняем запрос
        self.cursor.execute(f'''SELECT unit.name, minimum_unit FROM unit 
            JOIN sweets on sweets.unit_id = unit.id WHERE sweets.id = {id}''')
        data = self.cursor.fetchone()

        if data:
            name_unit = data[0]  # name
            min_unit = int(data[1])  # minimum_unit
            return [name_unit, min_unit]
        else:
            return None

    def query_opr_id(self, table_name, value):
        # Используем параметризированный запрос для защиты от SQL-инъекций
        query = f"SELECT ID FROM {table_name} WHERE Название = ? GROUP BY ID;"
        self.cursor.execute(query, (value,))
        result = self.cursor.fetchall()
        if result:
            opr_id = result[0][0]
            return opr_id
        else:
            return None

    def get_holder(self, table_name):

        self.cursor.execute(f"PRAGMA table_info({table_name})")
        holders = self.cursor.fetchall()
        columns = [column[1] for column in holders]  # Второй элемент - это имя столбца

        return columns

    def get_integer_columns(self, table_name):
        query = f'PRAGMA table_info({table_name})'
        self.cursor.execute(query)
        integer_columns = [row[1] for row in self.cursor.fetchall()if row[2].upper() in 'INTEGER']
        return integer_columns

    def get_decimal_columns(self, table_name):
        query = f'PRAGMA table_info({table_name})'
        self.cursor.execute(query)
        decimal_columns = [row[1] for row in self.cursor.fetchall()if row[2].upper() in 'DECIMAL(8,2)']
        return decimal_columns

    def get_table_name(self):
        # Выполняем запрос к sqlite_master, чтобы получить имена всех таблиц
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

        # Извлекаем имена таблиц из результата запроса
        columns = [column[0] for column in self.cursor.fetchall()]
        return columns

    def query_delete_items(self, id, table_name, column):
        query = f'DELETE FROM {table_name} WHERE {column} = ?'

        self.cursor.execute(query, (id,))
        self.db.commit()

    def query_delete_column(self, table_name, id):
        try:
            query = f'DELETE FROM {table_name} WHERE ID = ?'

            self.cursor.execute(query, (id,))
            self.db.commit()

        except Exception as e:
            print(f"4 Ошибка при выполнении запроса: {e}")  # Обра



    def query_add_new_column(self, table_name, param):
        self.cursor.execute(f'INSERT INTO {table_name} VALUES{tuple(param)};')
        self.db.commit()

    def query_update_column(self, holders, param, table_name):
        id = param[0]
        param.pop(0)
        holders.remove('ID')
        for holder, value in zip(holders, param):
            self.cursor.execute(f"UPDATE {table_name} SET {holder} = ? WHERE ID = ?", (value, id))
            self.db.commit()



    def query_fields_for_comboBox(self, table_name):
        try:
            self.cursor.execute(f'SELECT Название FROM {table_name}')
            data = self.cursor.fetchall()
            result = [item[0] for item in data]
            return result
        except Exception as e:
            print(f"111 Ошибка при выполнении запроса: {e}")
            return []



    def incr(self, table_name):
        self.cursor.execute(f'SELECT MAX(id) FROM {table_name}')
        data = self.cursor.fetchall()[0][0]
        incr_id = 1 if data == None else data + 1
        return incr_id