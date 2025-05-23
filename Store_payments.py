from Payments import Payment
from datetime import datetime
import psycopg2
import requests
import re 


def clean_data(file):
    test = Payment()
    value = test.from_receipt(file).to_dict()

    date_obj = datetime.strptime(value['date'], '%d %b %Y').date()
    time_clean = re.sub(r'[^\d:]', '', value['time']) 
    time_obj = datetime.strptime(time_clean, '%H:%M').time()
    amount_clean = float(re.sub(r'[^\d.]', '', value['amount']))

    return {
        'amount':amount_clean,
        'time':time_obj,
        'date':date_obj
    }

host = "postgres"
database = "mydatabase"
username = "myuser"
password = "mypassword"
port = 5432
conn = None
cur = None
value = clean_data('image/receipt.jpg')
try:
    conn = psycopg2.connect(
        host="localhost",       # หรือชื่อ container ถ้าอยู่ใน docker เดียวกัน
        port=5432,
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    
    cur = conn.cursor() 
    # insert_script = "INSERT INTO payments (date, time, amount) VALUES (%s, %s, %s);"
    select_script = '''SELECT date, amount, "time", id, name FROM public.payments;'''
    # cur.execute(select_script)

    cur.execute(select_script)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cur.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Id = ", row[3], )


    # conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

# print(clean_data('receipt5.jpg'))