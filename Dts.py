from modelos_DTs.Aritmeticos import dt_esAritmetico
from modelos_DTs.cadenas import dt_esCadena, dt_cadenas

class Dts:

    def __init__(self, marshall, pr):
        self.marshall = marshall
        self.pr = pr

    def perteneceLista(self, caracter, lista):
        for elemento in lista:
            if caracter == elemento:
                return True
    
        return False
            
    def  esAritmetico(self, caracter):
        return dt_esAritmetico(self, caracter)
    
    def esCadena(self, caracter):
        return dt_esCadena(self, caracter)
    
    def cadenas(self, lexema):
        return dt_cadenas(self, lexema)  
    
