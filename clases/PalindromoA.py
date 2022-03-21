import unicodedata

class Palindromo:
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


ejercicio = Palindromo()
ejercicio.esPalindromo('Arde ya la yedra')
