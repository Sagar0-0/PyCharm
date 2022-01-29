import json

data = '{"sagar":112 ,"akash":211}'
print(data)
parsed = json.loads(data)
print(parsed['akash'])

# json.dump converts a python dict into a json file