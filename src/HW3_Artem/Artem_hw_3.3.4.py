#Добавить каждому ключу число равное длине этого ключа

slovo = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}

for key, value in slovo.items():
    print(f"{key} {len(key)}, {value}")


