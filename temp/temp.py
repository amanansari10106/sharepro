
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/countries"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "15399113dbmshd60e897db04f79bp1304fcjsn25108d5bcf8f"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)