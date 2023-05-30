import os
import re
from Marshall import Marshall
from Pr import Palabras_Reservadas
from tabla_simbolos import Tabla
'''marshall'''
#from Parser import Parser

class Uami:
    
    '''marshall'''
    #def __init__(self, venata):
    def __init__(self, mcadena):
        
        '''marshall'''
        #self.ventana = ventana
        self.pr = Palabras_Reservadas()
        self.marshall = Marshall(self.pr, self)
        self.tabla = Tabla(self.pr)
        '''marshall''' 
        #self.tabla.cargarPal_Res()

        # Atributos
        self.urlTpl = ""
        self.urlErr = ""
        self.urlObj = ""
        self.lineas = 0
        self.errores = 0

    
    #def crearArchivo(self):

    #def escribirArchivo(self, ruta, modo, texto):

    #def getArchivoTexto(self, ruta)

    def iniciaCompilacion(self):

        '''
        while self.ventana.fuenteUrl == "":
            self.ventana.guardarArchivo()

        cadRes = ""
        cadRes += "Inicia Compilacion: " + str(self.ventana.fuenteUrl) + "\n\n"
        self.ventana.escribirAreaResultado( cadRes )
        cadRes += "Creando Archivos Tupla, Error y Objeto...\n"
        self.ventana.escribirAreaResultado( cadRes )
        self.crearArchivos()
        cadRes += "Espere un momento por favor...\n"
        self.ventana.escribirAreaResultado( cadRes )
        '''

        