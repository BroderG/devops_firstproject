import request
try:
  requests.get('http://127.0.0.1:5000/stop_server')
except:
  return ''
try:
  requests.get('http://127.0.0.1:5001/stop_server')
except:
  return ''
