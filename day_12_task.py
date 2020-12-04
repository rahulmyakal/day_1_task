import json
x = '{"name": "Sachin","age": 18,"city": "Mumbai"}'
print(json.loads(x)) 

values = [1,2,3,4,5]
print(json.dumps(values))

values = {1:"A", 2:"B", 3:"C"}
print(json.dumps(values, indent=4))