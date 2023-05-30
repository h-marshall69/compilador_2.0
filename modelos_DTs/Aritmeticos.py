def dt_esAritmetico(self, caracter):
    operadores = [ "=", "-", "+", "/", "*", "%" ]
    return self.perteneceLista(caracter, operadores)

def dt_aritmeticos(self, lexema):

    cont = self.marshall.contador
    pos = self.marshall.uami.tabla.findSymbol(lexema)