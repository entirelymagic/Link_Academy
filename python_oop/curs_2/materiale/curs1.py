# Construiti clasa Wallet(portofel) care sa abstractizeze 
# Clasa detine urmatoarele implementari cu verificarile necesare:
# widthdaw - se scot bani din portofel
# addMoney - se adaga bani in portofel
# showBalance - se printeaza balanta curenta

class Wallet:
    def __init__(self):
        self.balance = 0

    def showBalance(self):
        print(self.balance)
    
    def addMoney(self, suma):
        self.balance = self.balance + suma
        
    def draw(self, extract):
        if self.balance - extract > 0:
            self.balance = self.balance - extract
        else:
            print("Insuffiecient fonds")
        




elvisWalletObject = Wallet()
# Balanta 0
elvisWalletObject.showBalance()
# Scad 100
elvisWalletObject.draw(1000)

elvisWalletObject.draw(10000000)

# Balanta ???
elvisWalletObject.showBalance()




