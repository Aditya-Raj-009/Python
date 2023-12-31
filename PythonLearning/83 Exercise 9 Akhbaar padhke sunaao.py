#
from win32com.client import Dispatch
import requests
import json

speak = Dispatch("SAPI.SpVoice") # class
url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ce995c3d3c8549faa99a6de178ec80de"

speak.speak("Let's Begin!")
news = requests.get(url).text   # convert to json.
news_dict = json.loads(news) # convert to python dictionary.
print(news_dict["articles"])   # accessing articles
arts = news_dict["articles"]
for i,article in enumerate(arts):
    speak.speak(article["title"])
    if i != len(article.keys())-1:
        speak.speak("Moving on to the next news....listen carefully!")

speak.speak("Thanks for listening.....")