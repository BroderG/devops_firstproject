import requests
# requests.post('http://127.0.0.1:5000/users/2', json={"user_name": "john"})

# res = requests.post('http://127.0.0.1:5000/users/5', json={"user_name": "raful"})
# print(res.json())


# res = requests.put('http://127.0.0.1:5000/users/5', json={"user_name": "raful"})
# # if res.ok:
# print(res.json())


# res = requests.delete('http://127.0.0.1:5000/users/5')
# # if res.ok:
# print(res.json())




# ---------------------- from deletedis.py
import pymysql
from datetime import datetime

now = datetime.now()

def add_user(user_id, username):
    creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
    schema_name = 'freedb_moshe123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_moshez', passwd='BF%SNrp8#c7k4Fs', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Getting user_id's data from table “users”
    cursor.execute("SELECT user_id FROM freedb_moshe123.users;")
    result = str(cursor.fetchone())
    print(result)

    # Iterating table and converting id's to dictionary int
    data = []
    data.append(int(result.strip("(',)")))
    for row in cursor:
        for i in row:
            try:
                resu = int(i)
                data.append(resu)
                break
            except:
                continue
    print(data)

    # Check if ID exists:
    if user_id in data:
        while user_id in data:
            user_id += 1
        cursor.execute(
            "INSERT INTO `freedb_moshe123`.`users` (`user_id`, `user_name`, `creation_date`) VALUES ('" + str(
                user_id) + "', '" + username + "', '" + creation_date + "')")
    else:
        cursor.execute(
            "INSERT INTO `freedb_moshe123`.`users` (`user_id`, `user_name`, `creation_date`) VALUES ('" + str(
                user_id) + "', '" + username + "', '" + creation_date + "')")


    cursor.close()
    conn.close()

add_user(1, "mike")


# ---------------------- from garbagio2.py

import pymysql


def get_name(user_id):
    schema_name = 'freedb_moshe123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_moshez', passwd='BF%SNrp8#c7k4Fs', db=schema_name)
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM freedb_moshe123.users WHERE (`user_id` = '"+ str(user_id) +"');")
    result = str(cursor.fetchone())
    print(result.strip("(',)"))
    conn.close()

get_name(1)