def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 4, 6, 8, 10))


def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(key)
        print(value)


calculate(a=3, b=5, c=9, d=7)


class Car:
    def __init__(self, **kwargs):
        self.make =