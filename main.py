import random

from type1 import type1
from type2 import type2
from type3 import type3


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

TYPES = [type1, type2, type3]

if __name__ == '__main__':
    chosenType = random.choices(TYPES,k=1)[0]
    chosenType()