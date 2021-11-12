import random
import time
def mk():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )
def rm():
    return (
        random.randint(1,80000) >= random.randint(75000,80000)
           )
branches = 1
while True:
    if mk():
        print('|'*branches+'\\')
        branches += 1
    elif ( branches != 1 and rm() ):
        print('|'*(branches-1)+'/')
        branches -= 1
    else:
        print('|'*branches)
    time.sleep(0.001)