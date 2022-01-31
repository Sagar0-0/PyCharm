import datetime
from win32com.client import Dispatch
import requests
import json


def read(str):
    '''helper method to speaks out the input string'''
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def getJson(URl):
    '''helper method to return the json dictionary from input url'''
    jsonStr = requests.get(URL).text
    parsed = json.loads(jsonStr)
    return parsed


def readData(articlesList):
    '''helper method to reads out the given articles list'''
    for article in articlesList:
        readTitle = f"Title: {article['title']}"
        read(readTitle)
        readDesc = f"Description: {article['description']}"
        read(readDesc)


def readArticles(url):
    ''' direct method to read all articles from url'''
    jsonDict = getJson(url)
    articlesList = jsonDict['articles']
    readData(articlesList)


if __name__ == '__main__':
    URL = "https://newsapi.org/v2/everything?q=android&apiKey=cdbba53bb0d34fa2a43789edbdf5feba"
    read(f"Latest news for date: {datetime.date.today()}")
    readArticles(URL)
