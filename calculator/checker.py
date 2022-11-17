def check(message: str):
    lst = ['+', '-', '*', '/', 'i', ' ']
    for i in message:
        if i.isdigit() or i in lst:
            continue
        else:
            return 0
    if 'i' in message:
        return 2
    else:
        return 1
