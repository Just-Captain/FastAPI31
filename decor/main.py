def func(): # <- функция 
    pass

class Human():
    def add_human(self): # <- метод класса
        pass

human = Human()

@human.add_human()
def primer():
    pass

"""
Декораторы в Python пишутся с использованием символа @ перед определенением функции, которую нужно декррировать.
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Функция {func.__name__} выполняется за {result_time}")
        return result
    return wrapper

@timer
def generator(start, end, one, two, kwargs):
    time.sleep(2)
    result = []
    for i in range(start, end):
        result.append(i)
    return result





def message(func):
    def wrapper(*args, **kwargs):
        print(f'До вызова функции {func.__name__}')
        result = func(*args, **kwargs)
        print(f'После вызова функции {func.__name__}')
        return result
    return wrapper

@message
def hello():
    print(f"Работает функция hello")


@message
def sum_num(x, y, name):
    print(name)
    return x + y

print(sum_num(5, 15,'sayha', name='nikita'))