from utils import hexadecimal
def branchsim():
    #branches = 1
    #step = 0
    front = ' '*16
    while True:
        output = front+'* '+hexadecimal(7)
        print(output)
        for _ in range(3):
            print(front+'| ')