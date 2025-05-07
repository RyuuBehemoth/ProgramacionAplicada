from classes import Calculator
myCalculator = Calculator()

while True:
    print("\nIgrese el numero de la operacion que desea realizar:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Cociente de una division\n5.Residuo de una division\n6.Salir")
    x = input()
    x = int(x)
    if x > 6:
        print("Elija una opcion valida\n")
        continue
    elif x <= 0:
        print("Elija una opcion valida\n")
        continue
    elif x == 6:
        exit()
    print("\nIngrese los numeros a operar:")
    a = input()
    b = input()
    myCalculator.operation(x,int(a),int(b))