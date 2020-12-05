a = [3, 7, 1, 9, 2, 4, 5, 12]
odd = []
even = []
# Your code here

for k, v in enumerate(a):
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
print(f"Odds: {odd}", f"\nEven: {even}")

odd1 = []
even1 = []
for number in range(len(a)):
    if a[number] % 2 == 0:
        even1.append(number)
    else:
        odd1.append(number)
print(f"Odds: {odd}", f"\nEven: {even}")

