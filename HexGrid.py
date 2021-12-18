from random import choice
from random import randrange

from Hex import HexTile


#
class HexGrid:

    # hexes lole
    myGrid = list()

    #
    def __init__(self):

        # TODO move elsewhere
        self.playerPosition = []

        self.mySizeMaxX = 3
        # self.mySizeMinX = 3

        self.mySizeY = 3

        # self.myGrid = {HexTile()}
        self.initGrid()

        T_Home = self.selectHomeTile()

    #
    def initGrid(self):

        for y in range(self.mySizeY):
            for x in range(self.mySizeMaxX):

                self.myGrid.append(HexTile())

                if x == 0:
                    self.myGrid[-1].myPosition[0] = 0
                else:
                    self.myGrid[-1].myPosition[0] = x / 2

                # working out y
                if y == 0:
                    self.myGrid[-1].myPosition[1] = 0
                else:
                    self.myGrid[-1].myPosition[1] = y / 2

                print("initGrid positions, X of this hex is: ",  self.myGrid[-1].myPosition[0], " y is: ",
                      self.myGrid[-1].myPosition[1])

    #
    def deterimineHomeTileRiver(self, _homeTile):

        # 6 is starts from within
        _homeTile.myRiver[0] = randrange(0, 7)

        # if the river starts in this hex it can't end here
        # this is just here for funzies
        if _homeTile.myRiver[0] == 6:
            _homeTile.myRiver[1] = randrange(0, 6)

        else:
            _homeTile.myRiver[1] = randrange(0, 7)

        # can't have a river flow to and from the same place
        # this should stop that
        while _homeTile.myRiver[0] == _homeTile.myRiver[1]:
            if _homeTile.myRiver[0] == 6:
                _homeTile.myRiver[1] = randrange(0, 6)

            else:
                _homeTile.myRiver[1] = randrange(0, 7)

        print("river is " + str(_homeTile.myRiver[0]) + " " + str(_homeTile.myRiver[1]))

    #
    def printRiverInfo(self, _tile):
        T_Return = "This tile "
        if _tile.myRiver[0] == -1:
            T_Return += "does not have a river flowing into it"

        else:
            T_Return += "has a river flowing from "

            if _tile.myRiver[0] == 0:
                T_Return += "the tile north of it"

            elif _tile.myRiver[0] == 1:
                T_Return += "the tile north east of it"

            elif _tile.myRiver[0] == 2:
                T_Return += "the tile south east of it"

            elif _tile.myRiver[0] == 3:
                T_Return += "the tile south of it"

            elif _tile.myRiver[0] == 4:
                T_Return += "the tile south west of it"

            elif _tile.myRiver[0] == 5:
                T_Return += "the tile north west of it"

            elif _tile.myRiver[0] == 6:
                T_Return += "starting from within the hex"

        if _tile.myRiver[1] == -1:
            T_Return += "\ndoes not have a river flowing out of it"

        else:
            T_Return += "\nhas a river flowing to "

            if _tile.myRiver[1] == 0:
                T_Return += "the tile north of it"

            elif _tile.myRiver[1] == 1:
                T_Return += "the tile north east of it"

            elif _tile.myRiver[1] == 2:
                T_Return += "the tile south east of it"

            elif _tile.myRiver[1] == 3:
                T_Return += "the tile south of it"

            elif _tile.myRiver[1] == 4:
                T_Return += "the tile south west of it"

            elif _tile.myRiver[1] == 5:
                T_Return += "the tile north west of it"

            elif _tile.myRiver[1] == 6:
                T_Return += "somewhere within the hex"

        return T_Return

    #
    def selectHomeTile(self):

        # TODO consider having it always be an inner hex
        T_Return = choice(self.myGrid)

        self.playerPosition.append(T_Return.myPosition[0])
        self.playerPosition.append(T_Return.myPosition[1])
        T_Return.isExplored = True

        # home tile always has a river going somewhere
        self.deterimineHomeTileRiver(T_Return)

        print("your home hex is X: ", T_Return.myPosition[0], " Y: ", T_Return.myPosition[1])

        return T_Return

    # TODO this shit broke
    # only works with ints 0-5
    # 0 north, 3 south, 5 north-west
    def moveParty(self, _dir):

        if _dir == 0:
            if self.playerPosition[1] > 0.5:
                self.playerPosition[1] -= 1
                print("moved")
            else:
                print("at the top")

        # DEBUG
        elif _dir == 1:
            if self.playerPosition[1] > 0.0 and self.playerPosition[0] < self.mySizeMaxX:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] -= 0.5
                print("moved")
            else:
                print("at the top / side")

        #
        elif _dir == 2:
            if self.playerPosition[1] < (self.mySizeY / 2) - 0.5 and self.playerPosition[0] < self.mySizeMaxX:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] += 0.5
                print("moved")
            else:
                print("at the top / side")

        elif _dir == 3:
            if self.playerPosition[1] < (self.mySizeY / 2) - 0.5:
                self.playerPosition[1] += 1
                print("moved")
            else:
                print("at the bottom")

        elif _dir == 4:
            if self.playerPosition[1] < self.mySizeY and self.playerPosition[0] > 0.0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] += 0.5
                print("moved")
            else:
                print("at the top / side")

        elif _dir == 5:
            if self.playerPosition[0] > 0.0 and self.playerPosition[1] > 0.0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] -= 0.5
                print("moved")
            else:
                print("at the top / side")
