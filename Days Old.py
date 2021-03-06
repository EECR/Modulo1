# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #Vamos a convertir las dos fechas dadas a dias y luego restarlas
    bd = ((year1 - 1) * 365.25) 
    if year1 % 4 == 0 and month1 > 2:
        bd = bd + 1
    i = month1 - 1
    while i > 0:
        bd = bd + daysOfMonths[i-1]
        i = i - 1
    bd = bd + day1
    cd = ((year2 - 1) * 365.25) 
    if year2 % 4 == 0 and month2 > 2:
        cd = cd + 1
    i = month2 - 1
    while i > 0:
        cd = cd + daysOfMonths[i-1]
        i = i - 1
    cd = cd + day2
    return int(cd - bd)
    
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
