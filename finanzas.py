from ingresos import ingresos
from egresos import egresos

Ingresos = ingresos()
Egresos = egresos()

while True:

    print("Oprima 1 para entrar sus ingresos")
    print("Oprima 2 para entrar sus egresos")
    print("Oprima 3 para revisar su informe")
    numero = int(input(" "))


    if numero == 1:
        ingresos = int(input("Entre la cantidas que quiere poner: "))

        Ingresos.aumentarIngresos(ingresos)
        
        verTotal = Ingresos.getMontoTotal()


        print(f"Ahora el total de ingresos es {verTotal}")
        print("")

    elif numero == 2:

        verTotal = int(verTotal)
        egresos = int(input("Digite la cantidad que quiere sacar: "))
        
        Egresos.aumentarEgresos(egresos)
        ingresoActual = Ingresos.getMontoTotal()
        egresoActual = Egresos.getMontoTotal()

        total = ingresoActual - egresoActual


        print(f"ahora su total es {total}")

    elif numero == 3:
        print(f"Sus ingresos son:   {ingresoActual}")
        print(f"Sus egresos son -{egresoActual}")
        print(f"Su balance en la cuenta es de {total}")

        print("------------------------------------------------------------------------------------")

