# hex neighbours laid out in order of N NE SE S SW NW
class HexTile:

    myColour = ""

    def __init__(self, _neighbours):

        # TODO needs rando
        self.myColour = "green"
    #     for i in range(6):
    #         self.myNeighbors[-1] = _neighbours[i]

    #
    def pushNeighbor(self, _neighbor):
        self.myNeighbors[-1] = _neighbor

    #
    def getNeighborByID(self, _ID):
        return self.myNeighbors[_ID]

    #
    # def assignAllNeighbors(self, _neighbors):
    #     ""
