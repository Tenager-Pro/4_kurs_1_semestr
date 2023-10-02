import sqlite3

# Подключаемся к базе test_db.sqlite, в нашем случае она отсутствует. Создадим её.
conn = sqlite3.connect('test_db.sqlite')
cursor = conn.cursor()
# Создаем таблицу пользователей
cursor.execute('CREATE TABLE users(ID INTEGER PRIMARY KEY ASC, login TEXT UNIQUE, pass TEXT)')
# Добавляем пользователя
cursor.execute('INSERT INTO users (login, pass) VALUES ("login", "pass")')
conn.commit()
conn.close()
