class egresos:
    def __init__(self):
        self.sumaFinal = 0
        self.sumaMovimientos = 0

    def aumentarEgresos(self, egresos):
        self.sumaFinal = self.sumaFinal + egresos
        self.sumaMovimientos =+ 1
        return self.sumaFinal

    def getMontoTotal(self):
        total = self.sumaFinal
        return total 