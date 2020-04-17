

result = 0
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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


    print (" Tienes ", result, "dias de edad")
      
daysBetweenDates(2012,1,1,2018,4,28)