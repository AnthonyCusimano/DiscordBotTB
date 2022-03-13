from random import randrange


# hex neighbours laid out in order of N NE SE S SW NW
class HexTile:

    #
    def __init__(self):

        self.myColour = self.determineHexColour()
        self.myPrimaryBiome = self.determineBiome()
        # self.myPrimaryBiome = "mountain"
        #
        # self.myRiver = [-1, -1]
        # self.determineRiverLocations()
        self.myPosition = [0, 0]

        self.isExplored = False

    #
    def determineBiome(self, _biomeType=0):
        # TODO need detail on how to deterime a biome type
        T_Rando = 0
        if _biomeType == 0:
            T_Rando = randrange(1, 9)
        else:
            T_Rando = _biomeType

        if T_Rando == 1:
            print("forest")
            return "forest"
        elif T_Rando == 2:
            print("grassland")
            return "grassland"
        elif T_Rando == 3:
            print("hills")
            return "hills"
        elif T_Rando == 4:
            print("mountain")
            return "mountain"
        elif T_Rando == 5:
            print("swamp")
            return "swamp"
        elif T_Rando == 6:
            print("desert")
            return "desert"
        elif T_Rando == 7:
            print("taiga")
            return "taiga"
        elif T_Rando == 8:
            print("lake")
            return "lake"

    #
    def determineHexColour(self):
        T_Rando = randrange(1, 8)
        if T_Rando < 5:
            return "Emerald"
        else:
            return "Red"

    #
    # def determineRiverLocations(self, _neighborRiver=0):
        # T_riverStart = randrange(1, 12)
        # if T_riverStart > 6:
        #     self.myRiver[0] = 1
        # no neighborRiver
    #   if _neighborRiver != 0:
    #        T_riverStart = randrange(1, 12)
    #        if T_riverStart < 7:
    #            self.myRiver[0] = T_riverStart

        # TODO how often should a new river begin in a hex?
    #    T_riverEnd = randrange(1, 36)
    #    if T_riverEnd < 7:
    #        self.myRiver[1] = T_riverEnd


