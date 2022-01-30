from win32com.client import Dispatch
import requests
import json


# helper method to speaks out the input string
def read(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


# helper method to return the json dictionary from input url
def getJson(URl):
    jsonStr = requests.get(URL).text
    parsed = json.loads(jsonStr)
    return parsed


# helper method to reads out the given articles list
def readData(articlesList):
    for article in articlesList:
        readTitle = f"Title: {article['title']}"
        read(readTitle)
        readDesc = f"Description: {article['description']}"
        read(readDesc)


# direct method to read all articles from url
def readArticles(url):
    jsonDict = getJson(url)
    articlesList = jsonDict['articles']
    readData(articlesList)


if __name__ == '__main__':
    URL = "https://newsapi.org/v2/everything?q=marvel&apiKey=cdbba53bb0d34fa2a43789edbdf5feba"
    readArticles(URL)
