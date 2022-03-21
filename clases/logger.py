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