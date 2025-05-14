class Bank:
    def __init__(self,balance):
        self.balance = balance

    def consult_balance(self):
        print(f"Saldo: {self.balance}")

    def add_balance(self,x):
        self.balance += x