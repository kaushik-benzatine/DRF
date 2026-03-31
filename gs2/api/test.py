import requests
import json
from django.views.decorators.csrf import csrf_exempt
data = {
  'name': 'Kaushik',
  'age': 25,
  'roll': 101,
  'city': 'Kolkata'
}
json_data = json.dumps(data)

update = {
  'id': 4,
  'name': 'kartik',
  'age': 25,
  'roll': 101111111,
  'city': 'Bankok'
}

# update
r = requests.post('http://127.0.0.1:8000/student/update/', json=update)
# r = requests.post('http://127.0.0.1:8000/student/create/', json=data)
print(f"Status Code: {r.status_code}")
print(f"Response Text: {r.text}")
print(f"Headers: {r.headers}")
print(f"{r.text}")

# if r.text:
#     print(f"JSON: {r.json()}")
# else:
#     print("Empty response!")