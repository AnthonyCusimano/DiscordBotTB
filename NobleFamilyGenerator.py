import HeraldryGenerator
import NameGenerators
from NameGenerators import FormLastName
from NameGenerators import FormFirstName

from random import randint


#
class NobleFamily:

    #
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

        for x in range(self.numChildren):
            T_Return.append(FormFirstName())
            print(T_Return[-1])

        return T_Return




    #
    def determineFamilyName(self):
        return FormLastName()
