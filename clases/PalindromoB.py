import unicodedata

class Palindromo:
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
    

p = Palindromo("radar") 
p.test()
p = Palindromo("sonar") 
print(p.test()) 