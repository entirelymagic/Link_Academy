A = [[2, 4, 5], [1, 3, 7], [6, 2, 8]]
B = [[1, 3, 1], [8, 9, 4], [5, 3, 2]]
C = []
# Your code here

for i in range(len(A)):
    C.append([])
    for j in range(len(A)):
        s = A[i][j] + B[i][j]
        C[i].append(s)

print(C)

