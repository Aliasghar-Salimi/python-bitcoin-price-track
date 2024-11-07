import matplotlib.pyplot as plt
import sqlite3
import schedule
import time

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

selecttime = 'select time from Bitcoin'
cursor.execute(selecttime)
time = cursor.fetchall()
x = []

for i in time:
    x.append(i[0])

selectprice = 'select price from Bitcoin'
cursor.execute(selectprice)
price = cursor.fetchall()
y = []

for i in price:
    y.append(i[0])

plt.ylabel("price")
plt.xlabel("time")
plt.title("bitcoin rate")
plt.plot(x, y)
plt.show()
