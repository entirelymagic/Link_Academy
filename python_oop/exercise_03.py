class Wallet:
    def __init__(self):
        self.balance = 0

    def showBalance(self):
        print(self.balance)

    def add_balance(self, amount):
        self.balance += amount


elvis_wallet = Wallet()
dragos_wallet = Wallet()

elvis_wallet.add_balance(1000)
dragos_wallet.add_balance(500)
elvis_wallet.showBalance()
dragos_wallet.showBalance()
