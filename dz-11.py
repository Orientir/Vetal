from time import time

def check_time_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start time")
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print("End time")
        print("Time: ", t2-t1)
        return result
    return wrapper


@check_time_decorator
def check_sym(sym, list_count, grade, text):
    """
    Check symbol in meta and return grade
    :param sym: int number
    :param list_count: list of two int numbers - valid and unvalid
    :param grade: int number
    :param text: string
    :return: int number - general grade
    """
    print("Start function")
    if 0 < sym < list_count[1]:
        print(f'Слишком короткий {text}')
        print("End function")
        return 0
    elif sym <= list_count[0]:
        print(f'оценка за к-во {text} - {grade}')
        return grade

result = check_sym(50, [30, 60], 10, 'text')

