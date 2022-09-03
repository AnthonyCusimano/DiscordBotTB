import HeraldryGenerator
import NameGenerators
from NameGenerators import FormLastName
from NameGenerators import FormFirstName

from random import randint


# currently just looking to generate a household consisting of members of one immediate family
# eventually it'd be nice to have some maternal heritage thrown in as well
# possibly eventually able to generate a family tree
class NobleFamily:

    # self.numChildren = 0
    def __init__(self):
        #
        self.numChildren = 0

    # https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/
    # https://towardsdatascience.com/5-levels-of-generating-weighted-random-numbers-in-python-80473c9b0df
    def getFamilyCurrentSize(self):
        # TODO weight
        self.numChildren = randint(1, 16)
        return self.numChildren

    def determineChildrenName(self):
        T_Return = []
        print(self.numChildren)

        # TODO protect T_Return from repeat names
        for x in range(self.numChildren):
            T_Return.append(FormFirstName())
            print(T_Return[-1])

        return T_Return

    # yoinked from NameGenerators
    def determineFamilyName(self):
        return FormLastName()
