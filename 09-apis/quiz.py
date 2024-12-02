import requests
import json 

url = 'https://opentdb.com/api.php?amount=1&type=multiple'
response = requests.get(url)
data = json.loads(response.text)

multiple_choice = data['results'][0]
print("Q: ", multiple_choice['question'])