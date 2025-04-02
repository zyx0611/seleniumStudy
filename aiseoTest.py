import requests
import json

url = 'https://api.aiseo.ai/v2/rewrite'
headers = {
    'Authorization': 'Bearer <Kp/aO4qTSTk7mRczPK7ty8BNGLBrF/OXxpd0zbo8y8lpDyLHPgDu0WbxGdG/Q4fUxfeqhrRrW9WdcvD3dzrfgzalHR9SVxZOA+ZYXkwC5ZI=>',
    'Content-Type': 'application/json'
}
data = {
    'text': '啦啦啦啦啦啦啦啦啦呃呃呃呃呃呃呃呃呃不不不不不不不不不',
    'audience': 'general',
    'formality': 'neutral',
    'intent': 'inform'
}
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', json.dumps(response))