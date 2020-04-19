def print_number(i):
    i = 9 - i
    esp = (" "," ","  ")
    num = ("0","0","0","0","0","*","*","*","*","*")
    n = num[:i+1] + esp + num[i+1:]
    print n

print_number(9)

value =12345678
k = 2
x = (value%10)/10.0
value = int(value / 10)
print(value), x