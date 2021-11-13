import random

def hexadecimal(size: int):
    return ''.join(random.choices('0123456789abcdef',k=size))
def mk():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )
def rm():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )