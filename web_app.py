# Web facing app of project

# Libraries: flask

from flask import Flask
from db_connector import get_name


app = Flask(__name__)

# Get user name function - receives user_id in url:
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    # User get_name from db_connector.py to check if the username returned equals to "None", if so, print html ID "error" and a message of no user + ID
    if str(get_name(user_id)) == 'None':
        return "<H1 id='error'>" + "no such user: " + user_id + "</H1>", 200
    # If above condition is not met, return html ID "user" + the user_name returned from db_connector get_user func.
    else:
        return "<H1 id='user'>" + str(get_name(user_id)) + "</H1>", 200


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)


