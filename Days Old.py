# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    if year2 > year1:
        result = int((year2 - year1) * 365.25)
    i = month1 + 2
    if i == 12:
        i = 0
    elif i == 13:
        i = 1
    while i != month1:
        result = result + daysOfMonths[i]
    if i == 11:
        i = 0
    else:
        i = i + 1
    if day1 < day2:
        result = result + day2 + (daysOfMonths[month1+1]-day1)
    print (" Tienes ", result, "dias de edad")
      
daysBetweenDates(2012,1,1,2018,2,28)
# Test routine

#def test():
    #test_cases = [((2012,1,1,2012,2,28), 58), 
                  #((2012,1,1,2012,3,1), 60),
                  #((2011,6,30,2012,6,30), 366),
                  #((2011,1,1,2012,8,8), 585 ),
                  #((1900,1,1,1999,12,31), 36523)]
    #for (args, answer) in test_cases:
     #   result = daysBetweenDates(*args)
        #if result != answer:
            #print ("Test with data:", args, "failed")
        #else:
            #print ("Test case passed!")

#test()