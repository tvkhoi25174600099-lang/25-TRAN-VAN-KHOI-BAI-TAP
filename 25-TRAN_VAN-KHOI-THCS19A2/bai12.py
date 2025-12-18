n = int(input())
m = int(input())
p = int(input())

A = []
B = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input()))
    A.append(row)

for i in range(m):
    row = []
    for j in range(p):
        row.append(int(input()))
    B.append(row)

C = []
for i in range(n):
    row = []
    for j in range(p):
        s = 0
        for k in range(m):
            s += A[i][k] * B[k][j]
        row.append(s)
    C.append(row)

print(C)

