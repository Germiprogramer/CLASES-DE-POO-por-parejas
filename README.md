# CLASES-DE-POO-por-parejas

Los miembros del grupo son Germán y Gonzalo.

El link al repositorio es el siguiente: https://github.com/Germiprogramer/CLASES-DE-POO-por-parejas.git

# EJERCICIO 1
## a. Palíndromo - método de clase
El código de este ejercicio es el siguiente:
```
import unicodedata

class Palindromo_a:
    def palindromo(self, N, M):
        if N < M:
            if self.palabra[N] == self.palabra[M]:
                self.palindromo(N+1, M-1)
            else:
                self.esPalindromo = False
        elif N > M:
            self.palindromo(N, M+1)
        else:
            if self.palabra[N] == self.palabra[M]:
                self.esPalindromo = True
            else:
                self.esPalindromo = False
    
    def esPalindromo(self, palabra):
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        palabra = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', palabra).translate(trans_tab))
        palabra = palabra.lower()
        self.palabra = palabra
        self.palindromo(0, len(palabra)-1)
        if self.esPalindromo == True:
            print("True")
        else:
            print("False")
```


# EJERCICIO 2
## b. Palíndromo - método de instancia
El código de este ejercicio es el siguiente:
```
import unicodedata

class Palindromo_b:
    def __init__(self, palabra):
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        palabra = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', palabra).translate(trans_tab))
        palabra = palabra.lower()
        self.palabra = palabra

    def palindromo(self, N, M):
        if N < M:
            if self.palabra[N] == self.palabra[M]:
                self.palindromo(N+1, M-1)
            else:
                self.test = False
        elif N > M:
            self.palindromo(N, M+1)
        else:
            if self.palabra[N] == self.palabra[M]:
                self.test = True
            else:
                self.test = False
    
    def test(self):
        self.palindromo(0, len(self.palabra)-1)
        if self.test == True:
            print("True")
        else:
            print("False")
        print(self.palabra.upper())
```        

# EJERCICIO 3
## c. Puzzle

# EJERCICIO 4
## d. Logger
El código de este ejercicio es el siguiente:
```
class Test:
    def llamada(self, mensaje, x):
        Logger.log(mensaje, x)
    
class Logger:
    def log(mensaje, x):
        f = open('cat log.txt', "a+", encoding="utf-8")
        if x == 1:
            f.write('--Start log--')
            f.write('\n')
        f.write(mensaje)
        f.write('\n')
        if x == 5:
            f.write('--End log: ')
            f.write(str(x))
            f.write(' log(s) --')
            f.close
```            
