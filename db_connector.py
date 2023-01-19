# The DB connector with all the functions used by web_app and rest_app

# Libraries: pymysql, datetime, sys
import pymysql, sys
from datetime import datetime

# Assign the current time to "now" variable
now = datetime.now()

user = str(sys.argv[1])
passwd = str(sys.argv[2])

# A function to retrieve the user_name from the DB by ID
def get_name(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user=user, passwd=passwd, db='freedb_moshe123')
    conn.autocommit(True)
    cursor = conn.cursor()
    # Execute a statement to place the cursor on the user_name of the ID value given
    cursor.execute("SELECT user_name FROM freedb_moshe123.users WHERE (`user_id` = '"+ str(user_id) +"');")
    # Get one result, cast it to string and assign to variable "result"
    result = str(cursor.fetchone())
    # Return the result, after stripping it from any special characters
    return(result.strip("(',)"))
    cursor.close()
    conn.close()

# A function to add a user_name to the DB with provided user_name and ID
def add_user(user_id, username):
    # Take current time, change to specified format, and assign to variable "creation_date"
    creation_date = now.strftime("%Y-%m-%d %H:%M:%S")
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user=user, passwd=passwd, db='freedb_moshe123')
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Getting user_id's data from table “users”
    cursor.execute("SELECT user_id FROM freedb_moshe123.users;")
    # Get one result, cast it to string and assign to variable "result"
    result = str(cursor.fetchone())
    # Iterating table and converting id's to dictionary int
    data = []
    data.append(int(result.strip("(',)")))
    for row in cursor:
        for i in row:
            try:
                # Assign current position's character to int, if successful, append the int to "data" dictionary, then break the loop
                resu = int(i)
                data.append(resu)
                break
            except:
                continue

    # Check if ID exists in the above dictionary ("data"),if so, change ID number and then send the cmd to DB:
    if user_id in data:
        # As long as ID exists, add +1 to user_id and try again
        while user_id in data:
            user_id += 1
        # Inserting data into table
        cursor.execute(
            "INSERT INTO `freedb_moshe123`.`users` (`user_id`, `user_name`, `creation_date`) VALUES ('" + str(
                user_id) + "', '" + username + "', '" + creation_date + "')")
        return user_id
    # If above condition not met, send cmd to DB to add new user by ID + user_name + creation_date, and then return the current user_id value
    else:
        # Inserting data into table
        cursor.execute(
            "INSERT INTO `freedb_moshe123`.`users` (`user_id`, `user_name`, `creation_date`) VALUES ('" + str(
                user_id) + "', '" + username + "', '" + creation_date + "')")
        return user_id

    cursor.close()
    conn.close()

# A function to update a user_name to the DB with provided user_name and ID
def update_user(user_id, username):
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user=user, passwd=passwd, db='freedb_moshe123')
    conn.autocommit(True)
    cursor = conn.cursor()
    # Getting user_id's data from table “users”
    cursor.execute("SELECT user_id FROM freedb_moshe123.users;")
    result = str(cursor.fetchone())
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
    # Check if ID exists in the above dictionary ("data"), if so, execute command to update the user_name by ID in the DB, and return 1 to confirm
    if user_id in data:
        cursor.execute("UPDATE freedb_moshe123.users SET user_name = '" + username + "' WHERE user_id = '" + str(
            user_id) + "'")
        return 1
    # If ID does not exist, return 0 to initiate error response
    else:
        return 0
    cursor.close()
    conn.close()

# A function to delete a user from the DB by provided ID
def delete_user(user_id):
    # schema_name = 'freedb_moshe123'  # DELETE?
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user=user, passwd=passwd, db='freedb_moshe123')
    conn.autocommit(True)
    cursor = conn.cursor()
    # Getting user_id's data from table “users”
    cursor.execute("SELECT user_id FROM freedb_moshe123.users;")
    result = str(cursor.fetchone())
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
    # Check if ID exists in the above dictionary ("data"), if so, execute command to delete the user by the ID, and return 1 to confirm
    if user_id in data:
        cursor.execute("DELETE FROM freedb_moshe123.users WHERE user_id = '" + str(
            user_id) + "'")
        return 1
    # If ID does not exist, return 0 to initiate error response
    else:
        return 0

    cursor.close()
    conn.close()
