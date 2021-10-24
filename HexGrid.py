from Hex import HexTile


#
class HexGrid:

    # defaults
    # DEBUG this is overridden in __init on purpose atm
    mySizeMaxX = 5
    # mySizeMinX = 3

    mySizeY = 3

    #
    def __init__(self):

        self.mySizeMaxX = 3
        # self.mySizeMinX = 3

        self.mySizeY = 3

        # self.myGrid = {HexTile()}
        self.initGrid()

    #
    def initGrid(self):

        for x in range(self.mySizeMaxX):
            for y in range(self.mySizeY):
                print("in HexGrid.initGrid atm")
                print(x, "is X", "\n", y, " is Y")
