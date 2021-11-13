import random

from type1 import branchsim as type1
from type2 import branchsim as type2
from type3 import branchsim as type3

TYPES = [type1, type2, type3]

if __name__ == '__main__':
    chosenType = random.choices(TYPES,k=1)[0]
    chosenType()