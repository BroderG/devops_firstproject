import requests

try:
  requests.get('http://127.0.0.1:5000/stop_server')
except:
  print("Rest_app server not responding")
try:
  requests.get('http://127.0.0.1:5001/stop_server')
except:
  print("Web_app server not responding")
