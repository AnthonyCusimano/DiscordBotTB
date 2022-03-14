from random import choice
from random import randrange

from Hex import HexTile
from Time import Time


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

        #
        self.myRivers = list()

        # self.myGrid = {HexTile()}
        self.initGrid()

        T_Home = self.selectHomeTile()

    #
    def initGrid(self):

        # used to make sure we get a river starting from a mountain & hills
        T_MountainList = list()
        # TODO
        T_HillList = list()
        # swamps matter

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

                # river prio
                if self.myGrid[-1].myPrimaryBiome == "mountain":
                    # [-1] is fine cus we're still filling out the grid
                    T_MountainList.append(self.myGrid[-1])

                # some river prio
                elif self.myGrid[-1].myPrimaryBiome == "hills":
                    print("Hills don't have rivers yet, ignored")

                # print("initGrid positions, X of this hex is: ",  self.myGrid[-1].myPosition[0], " y is: ",
                #       self.myGrid[-1].myPosition[1])

        # starting the actual river
        # print(len(T_MountainList))
        T_RiverOdds = 0
        for x in T_MountainList:
            # 2/3 chance of having a river in each mountain
            # TODO randrange 1, 4
            T_RiverOdds = randrange(1, 3)
            if T_RiverOdds != 3:
                # T_MountainList[x].myRiver[0] = 0
                # self.myRivers.append([x])
                self.myRivers.append(list())
                self.myRivers[-1].append(x)

        # removing mountains that don't have a river from the list
        # T_MountainList[:] = [nn for nn in T_MountainList if nn.myRiver[0] != 0]
        # print(len(T_MountainList))
        # print(len(self.myRivers))

        # using this list to begin our rivers
        # self.myRivers = T_MountainList + T_HillList
        self.riverStepTwo()

    # TODO order of operations is changing to determine rivers THEN home tile
    # def deterimineHomeTileRiver(self, _homeTile):
    #
    #     # 6 is starts from within
    #     _homeTile.myRiver[0] = randrange(0, 7)
    #
    #     # if the river starts in this hex it can't end here
    #     # this is just here for funzies
    #     if _homeTile.myRiver[0] == 6:
    #         _homeTile.myRiver[1] = randrange(0, 6)
    #
    #     else:
    #         _homeTile.myRiver[1] = randrange(0, 7)
    #
    #     # can't have a river flow to and from the same place
    #     # this should stop that
    #     while _homeTile.myRiver[0] == _homeTile.myRiver[1]:
    #         if _homeTile.myRiver[0] == 6:
    #             _homeTile.myRiver[1] = randrange(0, 6)
    #
    #         else:
    #             _homeTile.myRiver[1] = randrange(0, 7)
    #
    #     print("river is " + str(_homeTile.myRiver[0]) + " " + str(_homeTile.myRiver[1]))

    #
    def riverStepTwo(self):

        T_NextTileDelta = [0, 0]
        # T_LastNumber = 0
        # for reach river
        for n in self.myRivers:
            #
            for r in n:
                print("length of n")
                print(len(n))

                while len(n) == 1:
                    # print("In nested for loop within riverStepTwo, T_LastNumber is ", T_LastNumber)

                    # need to use some sort of attrition to cause rivers to become more likely to stop as they get larger
                    T_NextTile = randrange(0, 6)
                    if len(n) < 2:
                        print("detecting a one length river")
                        T_NextTile = randrange(0, 5)
                    # making sure you can't go right back into the same tile
                    # while T_NextTile + T_LastNumber == 5:
                    #     print("Protecting from going back a tile in river creation")
                    #     T_NextTile = randrange(0, 6)
                    # up
                    if T_NextTile == 0:
                        T_NextTileDelta[0] = 0
                        T_NextTileDelta[1] = -1
                    elif T_NextTile == 1:
                        T_NextTileDelta[0] = 0.5
                        T_NextTileDelta[1] = -0.5
                    elif T_NextTile == 2:
                        T_NextTileDelta[0] = 0.5
                        T_NextTileDelta[1] = 0.5
                    # down
                    elif T_NextTile == 3:
                        T_NextTileDelta[0] = 0
                        T_NextTileDelta[1] = 1
                    elif T_NextTile == 4:
                        T_NextTileDelta[0] = -0.5
                        T_NextTileDelta[1] = 0.5
                    elif T_NextTile == 5:
                        T_NextTileDelta[0] = -0.5
                        T_NextTileDelta[1] = -0.5

                    T_LastNumber = T_NextTile

                    # OoB check here
                    print("beginning OoB check")
                    # print(r.myPosition[0] + T_NextTileDelta[0], ", ", r.myPosition[1] + T_NextTileDelta[1])

                    # if 0 < r.myPosition[0] + T_NextTileDelta[0] > self.mySizeMaxX and \
                    #         0 < r.myPosition[1] + T_NextTileDelta[1] > self.mySizeY:
                    if 0 <= r.myPosition[0] + T_NextTileDelta[0] < self.mySizeMaxX / 2 and \
                            0 <= r.myPosition[1] + T_NextTileDelta[1] < self.mySizeY / 2:
                        print("through the OoB check")
                        print("rolled a ", T_NextTile)
                        T_XFactor = (r.myPosition[0] + T_NextTileDelta[0]) * 2.0
                        T_YFactor = (r.myPosition[1] + T_NextTileDelta[1]) * 2.0 * self.mySizeMaxX
                        print("X + Y is ", T_XFactor + T_YFactor)
                        n.append(self.myGrid[int(T_XFactor + T_YFactor)])

        print("End of river step 2, there are ", len(self.myRivers), " rivers")

        for r in self.myRivers:
            print(len(r))
            for h in r:
                print(h.myPosition[0], ", ", h.myPosition[1])
            # formatting
            print()

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
        # self.deterimineHomeTileRiver(T_Return)

        print("your home hex is X: ", T_Return.myPosition[0], " Y: ", T_Return.myPosition[1])

        return T_Return

    # only works with ints 0-5
    # 0 north, 3 south, 5 north-west
    def moveParty(self, _dir):

        T_XPosition = self.playerPosition[0] * 2
        T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX

        if _dir == 0:
            if self.playerPosition[1] > 0.5:
                self.playerPosition[1] -= 1

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")
            else:
                print("at the top")

        # DEBUG
        elif _dir == 1:
            if self.playerPosition[1] > 0.0 and self.playerPosition[0] < self.mySizeMaxX / 2:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] -= 0.5

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")

            else:
                print("at the top / side")

        #
        elif _dir == 2:
            if self.playerPosition[1] < self.mySizeY / 2 and self.playerPosition[0] < self.mySizeMaxX / 2:
                self.playerPosition[0] += 0.5
                self.playerPosition[1] += 0.5

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")

            else:
                print("at the top / side")

        elif _dir == 3:
            if self.playerPosition[1] < (self.mySizeY / 2) - 0.5:
                self.playerPosition[1] += 1

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")

            else:
                print("at the bottom")

        elif _dir == 4:
            if self.playerPosition[1] < self.mySizeY / 2 and self.playerPosition[0] > 0.0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] += 0.5

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")

            else:
                print("at the top / side")

        elif _dir == 5:
            if self.playerPosition[0] > 0.0 and self.playerPosition[1] > 0.0:
                self.playerPosition[0] -= 0.5
                self.playerPosition[1] -= 0.5

                print(str(self.playerPosition[0]) + " " + str(self.playerPosition[1]))
                print(str(T_XPosition) + " " + str(T_YPosition))
                print(str(T_XPosition + T_YPosition))

                print("should see in move " + str(T_YPosition + T_XPosition))
                T_XPosition = self.playerPosition[0] * 2
                T_YPosition = self.playerPosition[1] * 2 * self.mySizeMaxX
                self.myGrid[int(T_YPosition) + int(T_XPosition)].isExplored = True
                print("moved")

            else:
                print("at the top / side")
