import requests
import json

data = {
  'name': 'extra3',
  'age': 25,
  'roll': 101,
  'city': 'ncd'
}

update_data = {
  'id': 2,
  'name': 'kartik',
  'age': 25,
  'roll': 101111111,
  'city': 'Bankok'
}

delete_data = {
  'id': 13
}

# Send as dictionary - requests will handle JSON encoding
# r = requests.post('http://127.0.0.1:8000/st/', json=data)
# r = requests.patch('http://127.0.0.1:8000/st/', json=update_data)
r = requests.delete('http://127.0.0.1:8000/st/', json=delete_data)

print(f"Status Code: {r.status_code}")
print(f"Response Text: {r.text}")
print(f"Headers: {r.headers}")
print(f"{r.text}")
