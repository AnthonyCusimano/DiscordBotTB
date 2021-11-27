from random import choice

from Hex import HexTile


#
class HexGrid:

    # defaults
    # DEBUG this is overridden in __init on purpose atm
    # mySizeMaxX = 5
    # mySizeMinX = 3

    # mySizeY = 3

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

        for x in range(self.mySizeMaxX):
            for y in range(self.mySizeY):
                #
                self.myGrid.append(HexTile())
                # TODO this is where we fix everything lole
                self.myGrid[-1].myPosition[0] = x
                self.myGrid[-1].myPosition[1] = y

    #
    def getPlayerPosition(self):
        T_Return = []
        T_XValue = 0
        if self.playerPosition[0] == 0:
            T_XValue = 0
        # even number check
        elif self.playerPosition[0] % 2 == 0:
            ""
        # T_XValue = self.playerPosition[0] -
        # T_Return.append()

        return T_Return


    #
    def selectHomeTile(self):

        T_Return = choice(self.myGrid)

        self.playerPosition.append(T_Return.myPosition[0])
        self.playerPosition.append(T_Return.myPosition[1])
        T_Return.isExplored = True

        print("your home hex is X: ", T_Return.myPosition[0], " Y: ", T_Return.myPosition[1])

        return T_Return

    # only works with ints 0-5
    # 0 north, 3 south, 5 north-west
    def moveParty(self, _dir):

        if _dir == 0:
            if self.playerPosition[1] > 0:
                self.playerPosition[1] -= 1
                print("moved")
            else:
                print("at the top")

        # DEBUG
        elif _dir == 1:
            if self.playerPosition[1] > 0 and self.playerPosition[0] < self.mySizeMaxX:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] -= 0.5
                print("moved")
            else:
                print("at the top / side")

        #
        elif _dir == 2:
            if self.playerPosition[1] > 0 and self.playerPosition[0] < self.mySizeMaxX:
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
            if self.playerPosition[1] < self.mySizeY and self.playerPosition[0] > 0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] += 0.5
                print("moved")
            else:
                print("at the top / side")

        elif _dir == 5:
            if self.playerPosition[0] > 0 and self.playerPosition[1] > 0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] -= 0.5
                print("moved")
            else:
                print("at the top / side")
