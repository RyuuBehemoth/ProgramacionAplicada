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
