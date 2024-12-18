#!/usr/bin/python3

import requests
from pprint import pprint
# url = "https://jsonplaceholder.typicode.com/posts"
url ="http://localhost:8000/"
body= {
  "name": "SSSSSSSSSSSSSSSSSSSSSS",
  "price": 0,
  "count": 0,
  "id": 22,
  "category": "tools"
}
# body = {
#             "title" : "Make a POST call",
#             "body" : "Details of making post call ....",
#             "userId": 1
#        }
response = requests.post(url, data=body)
print(response.status_code)
pprint(response.json())
''''

curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "FFFFFFFFFFF",
  "price": 0,
  "count": 0,
  "id": 9,
  "category": "tools"
}'
