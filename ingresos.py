class ingresos:
    def __init__(self):
        self.sumaFinal = 0
        self.sumaMovimientos = 0

    def aumentarIngresos(self, ingresos):
        self.sumaFinal = self.sumaFinal + ingresos
        self.sumaMovimientos =+ 1
        return self.sumaFinal

    def getMontoTotal(self):
        total = self.sumaFinal
        return total 