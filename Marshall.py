from Dts import Dts
'''marshall'''
from Pr import Palabras_Reservadas

class Marshall:

    '''marshall'''
    #def __init__(self, pr, uami):
    def __init__(self, mcaracter):

        '''marshall'''
        #self.pr = pr
        #self.uami = uami
        #self.reportaError = GeneradorError(self.uami)
        #self.contenidoFuente = self.uami.ventana.getTextAreaFuente()
        
        self.pr = Palabras_Reservadas()
        self.contenidoFuente = mcaracter
        self.contador = 1
        self.buffer = {
            "pos_leida": 0,
            "longitud": 0,
            "cadena": ""
        }

        self.init()


    def init(self):
        self.contenidoFuente = self.contenidoFuente.split("\n")
        self.llenaBuffer()


    def llenaBuffer(self):
        if self.contador <= len(self.contenidoFuente):
            Cadena = self.contenidoFuente[self.contador - 1]

            if Cadena == "":
                Cadena = '\n'

            self.buffer['pos_leida'] = 0
            self.buffer['cadena'] = Cadena
            self.buffer['longitud'] = len(Cadena)

        else:
            self.buffer['pos_leida'] = 0
            self.buffer['cadena'] = "null"
            self.buffer['longitud'] = 0

    def leerCaracter(self):
        if self.buffer["pos_leida"] == self.buffer["longitud"]:
            self.contador += 1
            self.llenaBuffer()

        if self.buffer["longitud"] != 0:
            caracter = self.buffer["cadena"][self.buffer["pos_leida"]]
            self.buffer["pos_leida"] += 1
            return caracter
        
    def desleer(self):
            if self.buffer["pos_leida"] == 0:
                self.contador -= 1
                self.buffer["pos_leida"] = self.buffer["longitud"] 
            else:
                self.buffer["pos_leida"] -= 1

    def marshallico(self):
        lexema = self.leerCaracter()
        dts = Dts(self, self.pr)

        if dts.esAritmetico(lexema):
            print(lexema)
            '''marshall'''
            # self.uami.lineas = self.contador
            return dts.aritmeticos(lexema)
        
        elif dts.esCadena(lexema):
            
            '''marshall'''
            #self.uami.lineas = self.contador
            respuesta = dts.cadenas(lexema)
            print(respuesta)
            if type(respuesta) == type(dict()):
                #self.reportaError.erroresLex(respuesta)
                return self.marshallico()
            return respuesta

if __name__ == '__main__':
    prueba_m = Marshall("\"marshall\"")
    print(prueba_m.marshallico())
