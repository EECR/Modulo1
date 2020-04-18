# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))
    
def smaller(a, b):
    if a < b:
        return a
    else:
        return b
        
def smallest(a, b, c):
    return smaller(a, smaller(b, c))

def median(a,b,c):
    x = 0
    z = 0
    x = smallest(a, b, c)
    z = biggest(a, b, c)
    if x < a and z > a:
        return a
    else:
        if x < b and z > b:
            return b
        else:
            return c
    




print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(2,2,1))
#>>> 7




