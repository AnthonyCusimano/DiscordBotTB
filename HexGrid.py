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

        print(T_Home.myPosition[0], ' ', T_Home.myPosition[1], T_Home.myPrimaryBiome)

    #
    def initGrid(self):

        for x in range(self.mySizeMaxX):
            for y in range(self.mySizeY):
                #
                self.myGrid.append(HexTile(0))
                self.myGrid[-1].myPosition[0] = x
                self.myGrid[-1].myPosition[1] = y

    #
    def selectHomeTile(self):

        T_Return = choice(self.myGrid)

        self.playerPosition.append(T_Return.myPosition[0])
        self.playerPosition.append(T_Return.myPosition[1])

        return T_Return

    # only works with ints 0-5
    # 0 north, 3 south, 5 north-west
    def moveParty(self, _dir):
        ""
        if self.playerPosition[1] > 0:
            self.myPlayerPosition[1] -= 1
