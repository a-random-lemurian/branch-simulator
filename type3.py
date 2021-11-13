import random
import time

HEXADECIMAL = 'abcdef1234567890'


def hexa():
    return ''.join(random.choices(HEXADECIMAL,k=7))

def singlebranch(maincm):
    for _ in range(maincm):
        print('* ',hexa())
        time.sleep(0.007)
    return

def twobranch(maincm,branchcm):
    print('|\\')
    for _ in range(maincm):
        print('*| ',hexa())
        time.sleep(0.007)
    for _ in range(branchcm):
        print('|* ',hexa())
        time.sleep(0.007)
    print('|/')
    return

def type3():
    while True:
        singlebranch(random.randint(1,66))
        twobranch(random.randint(3,79),random.randint(3,79))
