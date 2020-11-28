tax = 0.2
#Your code here

price = int(input("Enter your price: "))
VAT = tax*price
pret_final = price + VAT

print("Price with tax is " + str(pret_final))