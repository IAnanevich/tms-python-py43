import json

dict_j = {
    "123456": ("Mike", 23),
    "456789": ("Shaquille", 34),
    "095477": ("Jane", 50),
    "451200": ("Jack", 45),
    "181901": ("Monik", 27)
}
with open('lines.json', 'w') as file:
    json.dump(dict_j, file)
