import time


def log_input(data):
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(f'{time.ctime(time.time())}\tВвод: {data} =Вывод=> ')


def log_output(data):
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')


def log_upload():
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(f'{time.ctime(time.time())}\tВыгрузка логов\n')


def clear():
    with open('log.log', 'w', encoding='utf-8') as file:
        file.write('')
