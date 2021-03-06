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
<img width="185" alt="2022-03-21 (8)" src="https://user-images.githubusercontent.com/91720991/159346094-56de5db8-d974-4f77-b8c1-2254e0430978.png">



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
<img width="196" alt="2022-03-21 (7)" src="https://user-images.githubusercontent.com/91720991/159346015-f699de91-35b0-4e44-a6f4-c58767012818.png">


# EJERCICIO 3
## c. Puzzle

* print(y(a)) = esta devolviendo el valor a, que es un elemento de la clase A

* print(aa is a()) = retorna falso, porque son dos clases de A pero podrían pedir distintos atributos

* print(z(())) = es un elemento de una clase, por lo que su longitud f sera 0

* print(a().y((a,))) = la longitud es 1

* print(A.y(aa, (a,z))) = la longitud es 2

* print(aa.y((z,1,'z'))) = la longitud es 3

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

El UML de este ejercicio es el siguiente:

![ejr4](https://user-images.githubusercontent.com/91721237/159342206-e95801c7-4899-42c5-ac99-c43c5de315d0.jpg)
