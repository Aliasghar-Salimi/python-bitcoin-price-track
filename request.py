import schedule
import requests
import datetime
import sqlite3
import time

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

def the_request():    
    try:
        res = requests.request('GET', 'https://api.coincap.io/v2/assets')
        print(f"Status code: {res.status_code}")
        a = True
    except:
        print('something is wrong with your network!!!')
        a = False

    if a == True:
        content = res.json()
        data = content['data']
        bit = data[0]

        now = str(datetime.datetime.now())[:16]
        price = int(float(bit['priceUsd']))

        insert = f'insert into Bitcoin (time, price) values ("{now}", {price})'
        cursor.execute(insert)
        connection.commit()


schedule.every(1).minute.do(the_request)

while True:
    schedule.run_pending()
    time.sleep(1)



