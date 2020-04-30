# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    x = 1
    sublist = []
    lista_final = []
    lista = list(string)
    lista_final.append(lista[x-1])
    while x != (len(lista)):
        if lista[x-1] >= lista[x]:
            sublist.append(lista[x])
        else:
            lista_final.append(lista[x])
        if x+1 == len(lista):
            add_list(lista_final, sublist)
            print lista_final
            return lista_final
            break
        if lista[x+1] > lista[x]:
            add_list(lista_final, sublist)
            sublist = []
        x = x + 1
    return lista_final
    
def add_list(x, y):
    if len(y) > 0:
        x.append(y)
    return x
    
def list(string):    
    n = len(string)
    i = 0
    list = []
    while i != n:
        list.append(int(string[i]))
        i = i + 1
    return list


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1], 2, 3, [2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result