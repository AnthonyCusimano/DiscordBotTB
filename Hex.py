from random import randrange


# hex neighbours laid out in order of N NE SE S SW NW
class HexTile:

    #
    def __init__(self, _neighbours):

        self.myColour = self.determineHexColour()
        self.myPrimaryBiome = self.determineBiome()
        self.myRiver = [-1]
        self.myPosition = [0, 0]

        self.isExplored = False

    #
    def determineBiome(self):
        # TODO need detail on how to deterime a biome type
        T_Rando = randrange(1, 8)
        if T_Rando == 1:
            return "forest"
        elif T_Rando == 2:
            return "grassland"
        elif T_Rando == 3:
            return "hills"
        elif T_Rando == 4:
            return "mountain"
        elif T_Rando == 5:
            return "swamp"
        elif T_Rando == 6:
            return "desert"
        elif T_Rando == 7:
            return "taiga"
        elif T_Rando == 8:
            return "lake"

    #
    def determineHexColour(self):
        T_Rando = randrange(1, 8)
        if T_Rando < 5:
            return "Emerald"
        else:
            return "Red"
