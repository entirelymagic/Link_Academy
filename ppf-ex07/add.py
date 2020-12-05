a = [1, 2, 3]
b = [4, 5, 6]
# Your code here
c = []

for i in range(len(a)):
    t = a[i] + b[i]
    c.append(t)

print(c)

d = [x+y for x, y in zip(a, b)]

print(d)

