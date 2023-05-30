class Tabla:

    def __init(self, pr):
        self.pr = pr
        self.tope = 0
        self.tabla = []

    def findSymbol(self, lexema):
        indice = self.tope - 1
        for lista in reversed(self.tabla):
            if lexema == lista[0]:
                return indice
            
        return -1
    
    def getToken(self, pos):
        return self.tabla[pos][1]
    
    def getLexema(self, pos):
        return self.tabla[pos][0]
    
    def addItem(self, lexema, token):
        indice = self.tope
        self.tope += 1
        item = [lexema, token]
        self.tabla.append(item)
        return indice
    
    def imprimirTabla(self):
        indice = self.tope - 1

        cadTabla = [
            "\n\n",
            "<<<<<\tTabla\t>>>>>",
            "\n\n",
            "indice",
            "\t",
            "Lexema",
            "\t",
            "Token",
            "\n\n"
        ]

        for lista in reversed(self.tabla):
            texto = str(indice) + "\T" + "\t".join(lista) + "\n"
            cadTabla.append(texto)
            indice -= 1

    def cargarPal_Res(self):
        valores = self.pr.Reservadas.values()
        for valor in valores:
            self.addItem(valor, self.pr.P_RES)