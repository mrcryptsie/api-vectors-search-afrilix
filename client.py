import requests

url = "http://127.0.0.1:5000/query"
headers = {
    "Content-Type": "application/json"
}
data = {
    "query_texts": ["amour"],
    "n_results": 2
}

response = requests.post(url, json=data, headers=headers)
print(response.json())