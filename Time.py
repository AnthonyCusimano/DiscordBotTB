

#
class Time:

    #
    daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    #
    monthsOfTheYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]

    # number of days in each month
    numberOfDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # hours, minutes
    # starting at 8AM on day 0
    timeOfDay = [8, 0]
    # they called it March for this exact reason
    month = 2
    # don't 0 address this
    day = 1
    # days we've spent in this world
    totalDays = 0

    #
    def timeOfDayToString(self):
        T_Return = str(self.timeOfDay[0])
        T_Return += ':'

        if self.timeOfDay[1] == 0:
            T_Return += "00"

        else:
            T_Return += str(self.timeOfDay[1])

        return T_Return

    # TODO ranger check, road check, terrain modifier
    def HexMovementTimeChange(self):
        # by default 6 hours pass
        Time.timeOfDay[0] += 6
        self.manageOverFlows()

    #
    def monthOverflowCheck(self):
        #
        if Time.month > 11:
            Time.month -= 11

    #
    def dayOverflowCheck(self):
        if Time.day > Time.numberOfDays[Time.month]:
            Time.day -= Time.numberOfDays[Time.month]
            Time.month += 1

    #
    def hourOverflowCheck(self):
        if Time.timeOfDay[0] > 23:
            Time.day += 1
            Time.timeOfDay[0] -= 23
            Time.totalDays += 1

    #
    def minuteOverflowCheck(self):
        #
        if Time.timeOfDay[1] > 59:
            Time.timeOfDay[0] += 1
            Time.timeOfDay[1] -= 59

    #
    def manageOverFlows(self):
        print("in Time.manageOverFlows")
        self.minuteOverflowCheck()
        self.hourOverflowCheck()
        self.dayOverflowCheck()
        self.monthOverflowCheck()

    #
    def getMonthName(self):
        return Time.monthsOfTheYear[Time.month]
