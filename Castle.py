from random import randint

from NobleFamilyGenerator import NobleFamily


#
class Castle:

    #
    def __init__(self):
        self.myFamily = NobleFamily()
        self.mySize = self.determineMySize()

    #
    def determineMySize(self):
        T_Rando = randint(1, 10)

        # 30% smoll
        if T_Rando < 4:
            return 0

        # 40% medium
        elif T_Rando < 8:
            return 1

        # 30% beeg
        else:
            return 2
