import random
import time
hexadecimal = '0123456789abcdef'
def hexadecimal(size: int):
    return ''.join(random.choices(hexadecimal,k=size))
def mk():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )
def rm():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )
def type1():
    branches = 1
    step = 0
    while True:
        if mk():
            output = '|'*branches+'\\'
            branches += 1
        elif ( branches != 1 and rm() ):
            output = '|'*(branches-1)+'/'
            branches -= 1
        else:
            output = '|'*branches
        print(f'{branches:<6} {step:<8} {output:<60}')
        step += 1
        time.sleep(0.001)
def type2():
    branches = 1
    step = 0
    while True:
        print('* ',hexadecimal(7))
        for i in range(3):
            print('|')
if __name__ == '__main__':
    type1()