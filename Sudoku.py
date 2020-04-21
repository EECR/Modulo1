# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
                            
def factorial(n):
    fac = n
    while True:
        if n != 1:
            n = n - 1
            fac = fac * n
        else:
            return fac
            break

def num_consecutivos(n):
    total = 1
    for e in n:
        total = total * e
    return total

def consecutivos2(l, g):
    total = 1
    for e in l:
        total = total * e[g]
    return total

def check_column(y):
    n = len(y)
    while n > 0:
        k = consecutivos2(y, (n-1))
        if k != factorial(len(y)):
            return False
            break
        else:
            n = n - 1
    return True
               
def check_sudoku(l):
    n = len(l)
    for e in l:
        if n != len(e):
            return False
            break
        for x in e:
            #print x
            if type(x) != int:
                return False
                break
            if x < 0:
                return False
                break
        if factorial(len(e)) != num_consecutivos(e):
            return False
            break
    if check_column(l) == False:
        return False
    else:
        return True    


#print check_column(incorrect3)
    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
