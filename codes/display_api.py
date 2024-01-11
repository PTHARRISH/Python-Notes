import requests,json
response_API = requests.get('https://public-api.solscan.io/tools/inspect?message=hai')
print(response_API.text)
