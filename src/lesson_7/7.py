# «0b1011001»
# «0x59»
# o -> 010101001 -> o

# encode() - закодировать / decode() - раскодировать

# import string
#
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)

# unicode
# 1000
# utf - 8
# utf - 16
# utf - 32

# Привет, мир

# a = 'Привет мир'
# b = a.encode('utf-8')
# print(b)
# c = a.encode('utf-16')
# print(c)
# print(b.decode('utf-8'))
# print(b'\xd0'.decode())

# a = 'Hello'
# b = a.encode('utf-16')
# print(b.decode('utf-8'))

# print('Ёжик в тумане'.encode())  # эскейп-последовательность
# print('Ёжик в тумане'.encode().decode('utf-16'))


# print(ascii(12))
# print(ascii('cat'))
# print(ascii('кот'))

# print(str(123))
# print(str(b'\xd0\x9f\xd0\xb0\xd0\xb9\xd1\x82\xd0\xbe\xd0\xbd', 'utf-8'))

# print(bytes('python', 'ascii'))
# print(bytes('питон', 'utf16'))
# print(bytes([1, 2, 3]))

# import unicodedata
#
# print(unicodedata.name('я'))
# print(unicodedata.lookup('BOY'))
# print(unicodedata.lookup('Trigram for Heaven'))


# a = bytes((80, 77, 99, 101))
# print(a)
# print(bytes(1))
# print(bytes(2))
# print(bytes(3))
# print(a.decode('utf-8'))

# string = 'pythön!'
#
# a1 = string.encode(encoding='ascii', errors='replace')
# a2 = string.encode(encoding='ascii', errors='ignore')
# a3 = string.encode(encoding='ascii', errors='strict')
# print(a1)
# print(a2)
# print(a3)

# print(file.read(1))
# print(file.read())
# for line in file:
#     print(line)
# file.close()

# file = open('test.txt', 'r+')
#
# try:
#
#     print(file.read())
# except FileNotFoundError:
#     pass
# finally:
#     file.close()


# with open('test.txt', 'r+') as file:  # контекстный менеджер
#     # print(file.readline())
#     # file.seek(0)
#     # print(file.readline())
#     # print(file.readlines())
#     temp = file.read().splitlines()
#     # temp = file.read().split('\n')
#
#     print(temp)


import json

# data = {
#   "access": [
#     "switchport mode access",
#     "switchport access vlan",
#     "switchport nonegotiate",
#     "spanning-tree portfast",
#     "spanning-tree bpduguard enable"
#   ],
#   "trunk": [
#     "switchport trunk encapsulation dot1q",
#     "switchport mode trunk",
#     "switchport trunk native vlan 999",
#     "switchport trunk allowed vlan"
#   ]
# }

#
# with open('test.json', 'r') as file:
#     # file.write(json.dumps(data))
#     # json.dump(data, file)
#     # data = json.load(file)
#     file_content = file.read()
#     data = json.loads(file_content)
#
# print(file_content)
# for key, value in data.items():
#     print(f'{key}: {value}')


# import csv
#
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': None
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]


# with open('test.csv', 'w') as file:
# reader = csv.reader(file)
# print(list(reader))
# headers = next(reader)
# print(headers)
# print('-'*15)
# for line in reader:
#     print(line)
# reader = csv.DictReader(file)
# for line in reader:
#     print(line)
#     print(line['hostname'], line['model'])
# writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
# writer.writeheader()
# for line in data:
#     writer.writerow(line)


# with open('test.csv') as file:
#     reader = csv.DictReader(file)
#     print(list(reader))


# import openpyxl


# wb = openpyxl.load_workbook('test.xlsx')
# print(wb)
# sheet_1 = wb.active
# print(sheet_1)
# print(sheet_1['B2'].value)
#
# sheet_2 = wb.create_sheet('Sheet2')  # create new
# sheet_2.title = 'NewSheet2'
# print(wb.sheetnames)
#
# sheet_2 = wb.copy_worksheet(sheet_1)

# wb.remove(wb['name of sheet'])

# value = sheet_1['A5']
# print(sheet_1['C5'].column)
# print()
# value.value *= 2
#
#
# wb.save('test.xlsx')


# from tempfile import NamedTemporaryFile
#
# wb = openpyxl.load_workbook('')
#
# with NamedTemporaryFile() as file:
#     pass
