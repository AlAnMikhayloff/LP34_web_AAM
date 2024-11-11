import csv
import sqlite3


# Подключение к базе данных SQLite
conn = sqlite3.connect('webapp.db')
cursor = conn.cursor()

# Выполнить SQL-запрос
query = "SELECT * FROM user_data_set"
cursor.execute(query)
data = cursor.fetchall()

# Записать данные в CSV-файл
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])  # Write header
    writer.writerows(data)  # Write data rows

# Закрыть подключение к базе

conn.close()
