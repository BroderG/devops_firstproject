# Backend testing script

# Libraries: requests, json, time, pymsysql
import requests, json, time, pymysql


# User_name and ID variables to change for testing
user_name = "johnny"
user_id = 2
# Post a new user data to the REST API using POST method with variables from above, and save response to "res" variable
res = requests.post('http://127.0.0.1:5000/users/'+str(user_id), json={"user_name": user_name})
# Assign a dictionary, by loading the json response and converting it
tempdict = json.loads(json.dumps(res.json()))
# Check if "status" key equals to "error", if so print reason for failure.
if tempdict["status"] == "error":
    print("User ID was taken, instead assigned to a different ID, test cancelled")
    raise Exception("test failed")
# If above condition not met, wait 1 second, then send a get request and save response to "res" variable
else:
    time.sleep(1)
    res = requests.get('http://127.0.0.1:5000/users/'+str(user_id))
    # Assign a dictionary, by loading the json response and converting it
    tempdict = json.loads(json.dumps(res.json()))
    # Check if both the status code is 200, and user_name from response equals to initial user_name, if so continue test
    if res.status_code == 200 and tempdict["user_name"] == user_name:
        # schema_name = 'freedb_moshe123'
        # Establishing a connection to DB
        conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_moshez', passwd='BF%SNrp8#c7k4Fs',
                               db='freedb_moshe123')
        conn.autocommit(True)
        cursor = conn.cursor()
        # name = [] # DELETE??
        # Execute command in DB to retrieve user_name from DB and compare to initial user_name
        cursor.execute("SELECT user_name FROM freedb_moshe123.users WHERE (`user_id` = '" + str(user_id) + "');")
        result = str(cursor.fetchone())
        result.strip("(',)")
        conn.close()
        # If the retrieved user_name from DB equals the initial user_name, print message
        if result.strip("(',)") == user_name:
            print("everything ok")
        # If above condition not met, print reason for failure
        else:
            print("Failed last step - user_name in DB does not match initial user_name")
            raise Exception("test failed")
    else:
        print("Failed step - HTTP code not 200 / Response user_name does not match intial user_name")
        raise Exception("test failed")
