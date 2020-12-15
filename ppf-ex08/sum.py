d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'c': 300, 'a': 200, 'b': 400}

# Your code here
d3 = {}

for k in d1:
    if k in d2:
        r = d1[k]+d2[k]
        print(f'value of r is: {r}')
        d3[k] = r

print(d3)