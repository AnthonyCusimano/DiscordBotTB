import random


#
class FEDMGTables:

    #
    def __init__(self):
        """"""""

    #
    def randomDungeonStart(self):
        T_StartRando = random.randrange(9)
        if T_StartRando == 0:
            return "Square, 20 x 20ft.; passage on each wall"

        elif T_StartRando == 1:
            return "Square, 20 x 20ft.; door on two walls, passage in third wall"

        elif T_StartRando == 2:
            return "Square, 40 x 40 ft.; doors on three walls"

        elif T_StartRando == 3:
            return "Rectangle, 80 x 20ft., with row of pil lars down the middle; two passages leading from each " \
                   "long wall, doors on each short wall"

        elif T_StartRando == 4:
            return "Rectangle, 20 x 40ft.; passage on each wall"

        elif T_StartRando == 5:
            return "Circle, 40ft. diameter; one passage at each cardinal direction"

        elif T_StartRando == 6:
            return "Circle, 40ft. diameter; one passage in each cardinal direction; well in middle of room (might" \
                   "lead down to lower level)"

        elif T_StartRando == 7:
            return "Square, 20 x 20ft.; door on two wal ls , passage on third wall, secret door on fourth wall"

        elif T_StartRando == 8:
            return "Passage, 10 ft. wide; T intersection"

        elif T_StartRando == 9:
            return "Passage, 10ft. wide; four-way intersection"

    #
    def randomDungeonPassage(self):
        T_PassRando = random.randrange(19)
        T_Return = ""

        if T_PassRando < 2:
            T_Return = "Continue straight 30ft., no doors or side passages"
        elif T_PassRando == 2:
            T_Return = "Continue straight 20ft., door to the right, then an additional 10 ft. ahead"
        elif T_PassRando == 3:
            T_Return = "Continue straight 20ft., door to the left, then an additional 10 ft. ahead"
        elif T_PassRando == 4:
            T_Return = "Continue stra ight 20ft.; passage ends in a door"
        elif T_PassRando < 6:
            T_Return = "Continue straight 20ft., side passage to the right.then an additional 10ft. ahead"
        elif T_PassRando < 9:
            T_Return = "Continue straight 20ft., side passage to the left, then an additionallO ft. ahead"
        elif T_PassRando == 9:
            T_Return = "Continue straight 20ft., comes to a dead end; 10 percent chance of a secret door"
        elif T_PassRando < 12:
            T_Return = "Continue straight 20ft., then the passage turns left and continues 10 ft."
        elif T_PassRando < 14:
            T_PassRando = "Continue straight 20ft., then the passage turns right and continues 10ft."
        elif T_PassRando < 19:
            T_PassRando = "Chamber (roll on the Chamber table)"
        # this should just be a call
        else:
            T_PassRando = "Stairs* (roll on the Stairs table)"

        return T_Return

    #
    def randomDungeonDoor(self):
        T_DoorRando = random.randrange(19)

        if T_DoorRando < 10:
            return "wooden door (not stuck)"
        elif T_DoorRando < 12:
            return "wooden door; barred, stuck, or locked"
        elif T_DoorRando == 12:
            return "stone door (not stuck)"
        elif T_DoorRando == 13:
            return "stone door; barred, stuck, or locked"
        elif T_DoorRando == 14:
            return "iron door (not stuck)"
        elif T_DoorRando == 15:
            return "iron door; barred, stuck, or locked"
        elif T_DoorRando == 16:
            return "portcullis"
        elif T_DoorRando == 17:
            return "portcullis; locked in place"
        elif T_DoorRando == 18:
            return "secret door"
        elif T_DoorRando == 19:
            return "secret door; barred, stuck, or locked"
