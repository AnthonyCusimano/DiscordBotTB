

#
class Time:

    # hours, minutes
    timeOfDay = [0, 0]
    # they called it March for this exact reason
    month = 3
    # don't 0 address this
    day = 1
    # days we've spent in this world
    totalDays = 0

    #
    def HexMovementTimeChange(self):
        """"""""

    #
    def hourOverflowCheck(self):
        if Time.timeOfDay[0] > 24:
            Time.day += 1
            Time.timeOfDay[0] -= 24
            Time.totalDays += 1

    #
    def dayOverflowCheck(self):
        # every day has 30 months? Nah
        if Time.day > 30:
            Time.month += 1
            Time.day -= 30
