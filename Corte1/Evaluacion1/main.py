from classes import Bank

while True:
    bank = Bank(500)
    print("\tIngrese la operacion que desea realizar\n1.Consultar su saldo\n2.Consignar saldo\n3.Reetirar saldo\n")
    o = int(input())
    if (o == 1):
        bank.consult_balance()
    elif (o == 2):
        print("\nIngrese el valor a depositar:")
        value = int(input())
        bank.add_balance(value)
    elif (o == 3):
        print("\nIngrese el valor a retirar:")
        value = int(input())
        bank.balance