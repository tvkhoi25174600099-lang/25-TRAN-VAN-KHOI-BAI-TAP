A = []
B = []

n = int(input())
for i in range(n):
    A.append(int(input()))

m = int(input())
for i in range(m):
    B.append(int(input()))

A_trong_B = True
for x in A:
    if x not in B:
        A_trong_B = False

B_trong_A = True
for x in B:
    if x not in A:
        B_trong_A = False

print(A_trong_B, B_trong_A)

giao = []
for x in A:
    if x in B:
        giao.append(x)

hieu = []
for x in A:
    if x not in B:
        hieu.append(x)

print(giao, hieu)
