import json

string_as_json_format = '{"answer": "Hello, user"}'
obj = json.loads(string_as_json_format)

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"ключа {key} в JSON нет")