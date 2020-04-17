# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 6.349838

#ENTER CODE BELOW HERE
#Convierto el numero en string y lo asigno a la variable y
y = str(x)
#Busco la posision donde se encuentra el punto del decimal
s = y.find(".")
#Compruebo si el siguiente numero despues del punto es un 5, 6,7 ,8 o 9
#Si encuntra uno de estos numeros lo ubicara en la posision 0 y le sumara un 1
#Si no lo encuentra devolvera un -1 que sumado al 1 de la formula dara 0
t1 = y[s + 1:s + 2].find("5") + 1
t2 = y[s + 1:s + 2].find("6") + 1
t3 = y[s + 1:s + 2].find("7") + 1
t4 = y[s + 1:s + 2].find("8") + 1
t5 = y[s + 1:s + 2].find("9") + 1
#Tomo nuevamente el numero inicial y le sumo los resultados de la variable t1 a t5.
#Si encuentro algun numero 5, 6 ,7 8 o 9 sumara un 1 de lo contrario sumara un 0.
#Almaceno este resultado en una nueva variable z, la cual es numerica
z = x + t1 + t2 + t3 +t4 + t5
#Convierto el numero en string
z = str(z)
#Busco el punto decimal del nuevo numero
k = z.find(".")
#Elimino lo que esta despues del punto decimal e imprimo el numero como string
r = z[:k]

print (r)
