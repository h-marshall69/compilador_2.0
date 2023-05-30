def dt_esCadena(self, caracter):
    if caracter == "\"":
        return True
    return False

def dt_cadenas(self, lexema):
    cont = self.marshall.contador

    if lexema == "\"":
        caracter = ""
        resto = ""

        while caracter != "\"" and cont == self.marshall.contador:
            resto += caracter
            caracter = self.marshall.leerCaracter() 

        if cont != self.marshall.contador:
            lexema = lexema + resto
            self.marshall.desleer()
            return {
                "token": self.pr.ERROR,
                "lexema": "falto cerrar la comilla " + lexema
            }
        else:
            lexema = lexema + resto + caracter

            pos = self.marshall.uami.tabla.findSymbol(lexema)

            if pos == -1:
                pos = self.marshall.uami.tabla.addItem(lexema, self.pr.STRINGS)

            return pos