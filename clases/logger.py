class Test:
    def llamada(self, mensaje, x):
        Logger.log(mensaje, x)
    
class Logger:
    def log(mensaje, x):
        f = open('cat log.txt', "a+", encoding="utf-8")
        if i == 1:
            f.write('--Start log--')
            f.write('\n')
        f.write(mensaje)
        f.write('\n')
        if i == 5:
            f.write('--End log: ')
            f.write(str(x))
            f.write(' log(s) --')
            f.close
test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada", i) 
   else: 
       test.llamada("{}ª llamada".format(i), i)