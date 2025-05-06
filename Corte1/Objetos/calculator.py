class Calculator:
    def add(self,a,b):
        return a + b
    def substract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        try:
            res = (a/b)
            return(res)
        except ZeroDivisionError:
            print("No puedes dividir entre cero")
    def module(self,a,b):
        try:
            res = (a%b)
            return(res)
        except ZeroDivisionError:
            print("No puedes dividir entre cero")
    def operation(self,x,a,b):
        if x == 1:
            print(f"Resultado:  {self.add(a,b)}")
        elif x == 2:
            print(f"Resultado: {self.substract(a,b)}")
        elif x == 3:
            print(f"Resultado: {self.multiply(a,b)}")
        elif x == 4:
            print(f"Resultado: {self.divide(a,b)}")
        elif x == 5:
            print(f"Resultado: {self.module(a,b)}")

myCalculator = Calculator()
bol = True
"""""
print(myCalculator.add(a,b))
print(myCalculator.substract(a,b))
print(myCalculator.multiply(a,b))
print(myCalculator.divide(a,b))
"""
while bol:
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