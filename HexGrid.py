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

        # does my river start in this tile
        T_RiverStartsHere = randrange(0, 4)

        _homeTile.myRiver[0] = randrange(0, 5)

        _homeTile.myRiver.append(randrange(0, 5))




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
            if self.playerPosition[1] > 0.0:
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
            if self.playerPosition[1] > 0.0 and self.playerPosition[0] < self.mySizeMaxX:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] += 0.5
                print("moved")
            else:
                print("at the top / side")

        elif _dir == 3:
            if self.playerPosition[1] < self.mySizeY:
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
