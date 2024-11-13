from webapp.db import db
from flask_login import current_user
from webapp.calculation.models import UserDataSet
import sqlite3

conn = sqlite3.connect('webapp.db')
cursor = conn.cursor()
# # # Выполнить SQL-запрос
current_user_csv = str(current_user)
cursor.execute('SELECT * FROM user_data_set WHERE user_id=?', (current_user_csv,))
data = cursor.fetchall()
print(str(current_user.id))
