from clases.logger import *
from clases.PalindromoA import *
from clases.PalindromoB import *

if __name__ == "__main__":
    while True:
        ejr = input("Escriba el numero del ejercicio que desea iniciar, a, b, c o d: ")
        try:
            ejr == 'a' or ejr == 'b' or  ejr == 'c' or ejr =='d'
        except:
            pass
        else:
            break
    if ejr == 'a':
        ejercicio = Palindromo_a()
        ejercicio.esPalindromo('Arde ya la yedra')
    elif ejr == 'b':
        p = Palindromo_b("radar") 
        p.test() 
    elif ejr == 'd':
        test = Test() 
        for i in range(1, 6): 
            if i == 1: 
                test.llamada("Primera llamada", i) 
            else: 
                test.llamada("{}ª llamada".format(i), i)