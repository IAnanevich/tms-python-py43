from subprocess import Popen


process_list = []

while True:
    print('1. Запустить 10 клиентов\n2. Закрыть клиентов\n3. Выйти')
    tmp = input('Выбери: ')

    if tmp == '1':
        for _ in range(10):
            process_list.append(Popen(['python3', 'select_client.py']))
            # process_list.append(Popen(['open', '-a', 'Terminal', 'select_client.py']))
        print('Запущено 10 клиентов')
    elif tmp == '2':
        for process in process_list:
            process.terminate()
        process_list.clear()
    elif tmp == '3':
        break
