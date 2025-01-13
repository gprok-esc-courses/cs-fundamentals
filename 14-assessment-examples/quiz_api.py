import requests
import html

url = 'https://opentdb.com/api.php?amount=5&type=multiple'

response = requests.get(url)
data = response.json() 
results = data['results']

for item in results:
    q = html.unescape(item['question'])
    print("Q:", q)
    ca = html.unescape(item['correct_answer'])
    print("CA: ", ca)
    for entry in item['incorrect_answers']:
        ia = html.unescape(entry)
        print("IA: ", ia)
    print()

