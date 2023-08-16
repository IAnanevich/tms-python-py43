import json

information = {
    123456: ('Ivan', 54),
    789012: ('Lena', 34),
    789011: ('Alex', 44),
    789056: ('Dana', 26),
    789018: ('Max', 41),
    789010: ('Lina', 40)
}

with open('katya_7_3.json', 'w') as new_file:
    new_file.write(json.dumps(information))

with open('katya_7_3.json', 'r') as new_file:
   print(json.loads(new_file.read()))