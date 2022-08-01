

# TODO
class HeraldryGenerator:

    #
    def __init__(self):
        """"""""

    def createField(self):
        T_Return = "on a "

        T_Return += "dark "

        T_Return += "Blue "

        T_Return += "Field."

        return T_Return

    #
    def createCharge(self):
        T_Return = "black "

        T_Return += "snowflake "

        return T_Return

    def createHeraldry(self):
        T_Return = self.createCharge()
        T_Return += self.createField()

        return T_Return
