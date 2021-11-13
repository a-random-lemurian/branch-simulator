import random

from type1 import branchsim as type1_
from type2 import branchsim as type2_
from type3 import branchsim as type3_

TYPES = [type1_, type2_, type3_]

if __name__ == '__main__':
    chosenType = random.choices(TYPES,k=1)[0]
    chosenType()