import json
import requests

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "3805f6bbabcb42b3a0c08a489baf603d"

params = {
    "country":"us",
    "apiKey": API_KEY
}

def apifunction(API_URl,params):
    response = requests.get(API_URL, params=params)
    if response.status_code==200:
        articles = response.json().get('articles',[])
        for index,article in enumerate(articles[:3],start=1):
            print(f"Article{index}:\n{json.dumps(article,sort_keys=True,indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")


apifunction(API_URL,params)

