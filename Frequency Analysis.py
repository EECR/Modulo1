# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def list_converter(string):
    list = []
    for e in string:
        list.append(e)
    return list
        
def finder(word, i):
    # Busca cantidad de letras i en la palabra word
    c = 0
    # c es el contador para las letras
    k = len(word)
    r = 0
    while True:
        #Creamos un lazo para encontrar todas las variables representadas por i en word
        #Cuando r llegue a -1 se para el lazo y entraga el resultado c
        r = word.find(i, r)
        if r >= 0:
            c = c + 1
            r = r + 1
        else:
            return c
            break
    
def freq_analysis(message):
    n = len(message)
    lista = list_converter(message)
    freq = 0
    alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" ,"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    freq_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    p = 0
    k = 0
    d = 0.00
    for e in message:
        p = alphabet.index(lista[k])
        c = finder(message, e)
        n = n *1.00
        d = (c/n)
        freq_list[p] = d
        k = k + 1
    return freq_list


#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
