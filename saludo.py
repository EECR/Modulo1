def print_number(i):
    i = 9 - i
    esp = (" "," ","  ")
    num = ("0","0","0","0","0","*","*","*","*","*")
    n = num[:i+1] + esp + num[i+1:]
    print n

print_number(9)
