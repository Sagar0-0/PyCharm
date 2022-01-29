import requests

requestResult = requests.get("https://github.com/Sagar0-0")
print(requestResult.text)
print(requestResult.status_code)
url = "https://github.com/Sagar0-0"
data = {
    'name': 'sagar'
    ,'cla':'cgc'
}
putRequest = requests.post(url=url,data=data)
print(putRequest)
