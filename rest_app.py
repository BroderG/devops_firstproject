# Backend facing app of project

# Libraries: flask, request

from flask import Flask, request
from db_connector import add_user, get_name, update_user, delete_user
# import json

app = Flask(__name__)


# supported methods receive user_id in url + json payload
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    # Get method to get a username
    if request.method == 'GET':
        # Use get_name function from db_connector.py and assign the name returned to "name" variable
        name = get_name(user_id)
        # Check if the "name" variable equals to "None", if so, return status error and reason in json format + generic error html status code
        if name == "None":
            return {'status': 'error', 'reason:': 'No such ID'}, 500  # status code
        # If above condition is not met, proceed to return user_id + user_name + OK html status code
        else:
            return {'user_id': user_id, 'user_name': name}, 200  # status code

    # Post method to enter a new username with new ID
    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # Use function "add_user" from db_connector.py with the user_id and user_name variables cast as int + str, and assign the returned output to "tmpid" variable
        tmpid = add_user(int(user_id), str(user_name))
        # Check if the returned user_id equals to the original user_id, if so, return status ok + OK html status code
        if int(user_id) == int(tmpid):
            return {'status': 'ok', 'user_added': user_name}, 200  # status code
        # If above condition is not met, return status error and the replacement ID the user_name has gotten + generic error html status code
        else:
            return {'status': 'error', 'reason:': 'ID already exists, instead assigned to ID: ' +str(tmpid)}, 500  # status code

    # Put method to update a username by ID
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # Use function update_user from db_connector.py with user_id and user_name variables cast as int + str, and assign the returned output to "tmp" variable
        tmp = update_user(int(user_id), str(user_name))
        # Check if returned value equals "1", if so, return status ok and user updated message in json format + OK html status code
        if int(tmp) == 1:
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        # If above condition is not met, return status error with reason + generic error html status code
        else:
            return {'status': 'error', 'reason:': 'No such ID'}, 500  # status code

    # Delete method to delete a username by ID
    elif request.method == 'DELETE':
        # Use function delete_user from db_connector.py with user_id variable cast as int, and assign the returned output to "tmp" variable
        tmp = delete_user(int(user_id))
        # Check if returned value equals "1", if so, return status ok and user deleted message + OK html status code
        if int(tmp) == 1:
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        # If above condition is not met, return status error with reason + generic error html status code
        else:
            return {'status': 'error', 'reason:': 'No such ID'}, 500  # status code


app.run(host='127.0.0.1', debug=True, port=5000)