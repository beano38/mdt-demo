import requests

URL = "https://webexapis.com/v1/messages"
ROOM_ID = "5453daf0-e578-11eb-b31c-8f9d0ae3efb6"
TOKEN = "OWIyMjEyMjgtMDk5OS00MTE5LWEyNjgtZDUyNjc5NzZmYjQwNWVlNTZmNzctYzYx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"


payload = {
  "roomId": "5453daf0-e578-11eb-b31c-8f9d0ae3efb6",
  "text": "test"
}


payload = "{\r\n  \"roomId\" : \"5453daf0-e578-11eb-b31c-8f9d0ae3efb6\",\r\n  \"text\" : \"message\"\r\n}"
headers = {
  "Authorization": f"Bearer {TOKEN}",
  "Content-Type": "application/json"
}

response = requests.request("POST", URL, headers=headers, data=payload)

print(response.text.encode('utf8'))