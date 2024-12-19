import sqlite3

# Подключение к базе данных (если базы нет, она будет создана)
conn = sqlite3.connect('db_avto.db')
cursor = conn.cursor()

# Создание таблиц
cursor.executescript('''

-- Создание базы данных
CREATE TABLE Тип_трансмиссии (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT 
);

-- Таблица для типов привода
CREATE TABLE Тип_привода (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT 
);

-- Таблица для типов двигателя
CREATE TABLE Тип_двигателя (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT 
);

-- Таблица для марок автомобилей
CREATE TABLE Тип_марки (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT 
);

-- Таблица для моделей автомобилей
CREATE TABLE Тип_модели (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT,
    ID_Тип_марки INTEGER,
    FOREIGN KEY (ID_Тип_марки) REFERENCES Тип_марки(ID)
);

CREATE TABLE Тип_оплаты (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT 
);

-- Таблица для автомобилей
CREATE TABLE Автомобили (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Тип_модели INTEGER,
    Год INTEGER,
    VIN TEXT ,
    Цвет TEXT,
  	Фото TEXT,
    ID_Тип_двигателя INTEGER,
    Объем DECIMAL(8,2),
    Мощность INTEGER,
    ID_Тип_трансмиссии INTEGER,
    ID_Тип_привода INTEGER,
    Масса DECIMAL(8,2),
    Закуп DECIMAL(8,2),
    Цена DECIMAL(8,2),
    Комплектация TEXT,
    Статус TEXT ,
    FOREIGN KEY (ID_Тип_модели) REFERENCES Тип_модели(ID),
    FOREIGN KEY (ID_Тип_двигателя) REFERENCES Тип_двигателя(ID),
    FOREIGN KEY (ID_Тип_трансмиссии) REFERENCES Тип_трансмиссии(ID),
    FOREIGN KEY (ID_Тип_привода) REFERENCES Тип_привода(ID)
);

-- Таблица для клиентов
CREATE TABLE Клиенты (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя TEXT,
    Фамилия TEXT,
    Телефон TEXT ,
    Email TEXT ,
    Адрес TEXT,
    Серия_паспорта TEXT,
    Номер_паспорта DATE ,
    Дата_выдачи DATE,
    Кем_выдан TEXT
);

-- Таблица для сотрудников
CREATE TABLE Сотрудники (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя TEXT,
    Фамилия TEXT,
    Телефон TEXT ,
    Email TEXT ,
    Должность TEXT,
    Дата_рождения TEXT,
    Логин TEXT,
    Пароль TEXT,
    Статус TEXT
);

-- Таблица для продаж
CREATE TABLE Продажи (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Клиенты INTEGER,
    ID_Сотрудники INTEGER,
    ID_Автомобили INTEGER,
    Дата_продажи DATETIME,
    Цена DECIMAL(8,2),
    ID_Тип_оплаты INTEGER,
    FOREIGN KEY (ID_Клиенты) REFERENCES Клиенты(ID),
    FOREIGN KEY (ID_Сотрудники) REFERENCES Сотрудники(ID),
    FOREIGN KEY (ID_Автомобили) REFERENCES Автомобили(ID),
    FOREIGN KEY (ID_Тип_оплаты) REFERENCES Тип_оплаты(ID)
);




-- Типы трансмиссий
INSERT INTO Тип_трансмиссии (Название) VALUES
('Механическая'),
('Автоматическая'),
('Роботизированная'),
('Вариатор');

-- Типы привода
INSERT INTO Тип_привода (Название) VALUES
('Передний'),
('Задний'),
('Полный');

-- Типы двигателей
INSERT INTO Тип_двигателя (Название) VALUES
('Бензиновый'),
('Дизельный'),
('Гибридный'),
('Электрический');

-- Типы марок
INSERT INTO Тип_марки (Название) VALUES
('Toyota'),
('BMW'),
('Mercedes-Benz'),
('Volkswagen'),
('Ford');

-- Типы моделей
INSERT INTO Тип_модели (Название, ID_Тип_марки) VALUES
('Camry', 1),
('3 Series', 2),
('E-Class', 3),
('Golf', 4),
('Focus', 5);

-- Типы оплаты
INSERT INTO Тип_оплаты (Название) VALUES
('Наличные'),
('Кредит'),
('Лизинг'),
('Безналичный расчет');

INSERT INTO Сотрудники (Имя, Фамилия, Телефон, Email, Должность, Дата_рождения, Логин, Пароль, Статус) VALUES
('Олег', 'Кузнецов', '89034567890', 'oleg.kuznetsov@mail.ru', 'Руководитель', '1985-02-20', 'director', 'director', 'Активный'),
('Екатерина', 'Дмитриева', '89035678901', 'ekaterina.dmitrieva@mail.ru', 'Сотрудник', '1990-05-14', 'worker', 'worker', 'Активный'),
('Михаил', 'Сидоров', '89036789012', 'mikhail.sidorov@mail.ru', 'Сотрудник', '1982-11-30', 'misha_s', 'password789', 'Уволен');


-- Автомобили
INSERT INTO Автомобили (ID_Тип_модели, Год, VIN, Цвет, Фото, ID_Тип_двигателя, Объем, Мощность, ID_Тип_трансмиссии, ID_Тип_привода, Масса, Закуп, Цена, Комплектация, Статус) VALUES
(1, 2022, 'JT2BG22K0Y3023704', 'Синий', 'photo/camry.jpg', 1, 2.5, 200, 2, 1, 1500, 2500000, 3000000, 'Стандарт', 'Активный'),
(2, 2023, 'WBA5B12080JX12345', 'Черный', 'photo/bmv.jpg', 2, 3.0, 250, 2, 2, 1700, 3500000, 4500000, 'Премиум', 'Активный'),
(3, 2021, 'WDBUF82J0XA567890', 'Синий', 'photo/mers.jpg', 3, 2.0, 220, 1, 3, 1600, 3000000, 4000000, 'Люксовая', 'Активный'),
(4, 2022, 'WV2Z12478PH456789', 'Черный', 'photo/golf.jpg', 1, 1.8, 150, 3, 1, 1400, 2200000, 2800000, 'Спортивная', 'Активный'),
(5, 2020, '1FADP3F27JL123456', 'Черный', 'photo/ford.jpg', 2, 2.0, 180, 2, 2, 1450, 2100000, 2600000, 'Эконом', 'Активный');

-- Клиенты
INSERT INTO Клиенты (Имя, Фамилия, Телефон, Email, Адрес, Серия_паспорта, Номер_паспорта, Дата_выдачи, Кем_выдан) VALUES
('Иван', 'Петров', '89031234567', 'ivan.petrov@mail.ru', 'Москва, ул. Ленина, 15', '45 23', '123456', '2020-05-15', 'МВД России'),
('Анна', 'Смирнова', '89032345678', 'anna.smirnova@mail.ru', 'Санкт-Петербург, ул. Пушкина, 10', '12 34', '654321', '2019-03-20', 'УФМС Санкт-Петербурга'),
('Дмитрий', 'Иванов', '89033456789', 'dmitry.ivanov@mail.ru', 'Екатеринбург, ул. Мира, 5', '34 56', '987654', '2021-08-10', 'МВД России');



-- Триггер для изменения статуса автомобиля на "Продан" при добавлении в Продажи
CREATE TRIGGER Trigger_Продан_After_Insert
AFTER INSERT ON Продажи
FOR EACH ROW
BEGIN
    UPDATE Автомобили
    SET Статус = 'Продан'
    WHERE ID = NEW.ID_Автомобили;
END;

-- Триггер для изменения статуса автомобиля на "Активный" при удалении из Продаж
CREATE TRIGGER Trigger_Активный_After_Delete
AFTER DELETE ON Продажи
FOR EACH ROW
BEGIN
    UPDATE Автомобили
    SET Статус = 'Активный'
    WHERE ID = OLD.ID_Автомобили;
END;

CREATE VIEW Отчет_Выручка_За_Период AS
SELECT 
    DATE(Продажи.Дата_продажи) AS Дата_продажи,
    COUNT(Продажи.ID) AS Количество_Продаж,
    SUM(Продажи.Цена) AS Общая_Выручка
FROM Продажи
GROUP BY DATE(Продажи.Дата_продажи);





CREATE VIEW Отчет_Прибыль_За_Период AS
SELECT 
    Продажи.Дата_продажи,
    Тип_марки.Название AS Марка,
    Тип_модели.Название AS Модель,
    Автомобили.vin,
    Автомобили.Закуп AS Закупочная_Цена,
    Продажи.Цена AS Цена_Продажи,
    (Продажи.Цена - Автомобили.Закуп) AS Прибыль
FROM Продажи
LEFT JOIN Автомобили ON Продажи.ID_Автомобили = Автомобили.ID
LEFT JOIN Тип_модели ON Автомобили.ID_Тип_модели = Тип_модели.ID
LEFT JOIN Тип_марки ON Тип_модели.ID_Тип_марки = Тип_марки.ID;



CREATE VIEW Отчет_Продажи_Сотрудников AS
SELECT 
    Сотрудники.ID AS ID_Сотрудника,
    Сотрудники.Имя || ' ' || Сотрудники.Фамилия AS Сотрудник,
    Сотрудники.Должность,
    Продажи.Дата_продажи,
    COUNT(Продажи.ID) AS Количество_Продаж,
    SUM(Продажи.Цена) AS Общая_Выручка
FROM Продажи
LEFT JOIN Сотрудники ON Продажи.ID_Сотрудники = Сотрудники.ID
GROUP BY Сотрудники.ID, Сотрудники.Имя, Сотрудники.Фамилия, Сотрудники.Должность, Продажи.Дата_продажи;
  
  

''')

# Проверим, что таблицы созданы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Закрытие соединения
conn.commit()
conn.close()


