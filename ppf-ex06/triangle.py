
#Your code here

for i in range(1, H+1):
    for j in range(1, i+1):
        if j % 2:
            print('*', end='')
        else:
            print('#', end='')
    else:
        print('')
