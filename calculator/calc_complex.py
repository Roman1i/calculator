lst = ['+', '-', '*', '/']


def res(num, num2, operation):
    first = int
    second = int
    if operation == '+' or operation == '-':
        for i, item in enumerate(num):
            if item in lst and i != 0:
                first = int(num[:i])
                second = int(num[i:-1])
        for i, item in enumerate(num2):
            if item in lst and i != 0:
                first += int(num2[:i])
                second += int(num2[i:-1])
    elif operation == '*':
        for i, item in enumerate(num):
            if item in lst and i != 0:
                first = int(num[:i])
                second = int(num[i:-1])
        for i, item in enumerate(num2):
            if item in lst and i != 0:
                first *= int(num2[:i])
                second *= int(num2[i:-1])
    elif operation == '/':
        for i, item in enumerate(num):
            if item in lst and i != 0:
                first = int(num[:i])
                second = int(num[i:-1])
        for i, item in enumerate(num2):
            if item in lst and i != 0:
                first /= int(num2[:i])
                second /= int(num2[i:-1])
    if second > 0:
        return f'{first}+{second}i'
    elif second < 0:
        return f'{first}{second}i'
    elif second == 0:
        return f'{first}+0i'


def calculation(message: str):
    message_lst = message.split()
    for i, item in enumerate(message_lst):
        if item in lst:
            message_lst.insert(i-1, res(message_lst[i-1], message_lst[i+1], item))
            for j in range(3):
                message_lst.pop(i)
    return message_lst[0]
