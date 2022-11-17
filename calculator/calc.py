import checker
import calc_complex
import loger


def calculation(message: str):
    loger.log_input(message)
    if checker.check(message) == 1:
        loger.log_output(eval(message))
        return eval(message)
    elif checker.check(message) == 2:
        loger.log_output(calc_complex.calculation(message))
        return calc_complex.calculation(message)
    else:
        loger.log_output('Некорректный ввод')
        return 'Некорректный ввод'
