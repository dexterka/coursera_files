# Parse JSON data
import json

data = '''{ 
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
    "email" : {
        "hide" : "yes"
        }
} '''

info = json.loads(data)  # load as string, result is a dictionary

print(type(info))
print('Name:', info['name'])
print('Email hidden:', info['email']['hide'])


# Nested dictionaries within a list
input = '''[
    {  "id" : "001",
        "x"  : "2",
        "name" : "Chuck"
        },
    {   "id" : "009",
        "x"  : "7",
        "name" : "Brent"
        }
] '''

info = json.loads(input)  # list of dictionaries
print('User count:', len(info))

for item in info:
    print('Name:', item['name'])
    print('User ID:', item['id'])
    print('X:', item['x'])