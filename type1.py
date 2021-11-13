import time
from main import mk, rm
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