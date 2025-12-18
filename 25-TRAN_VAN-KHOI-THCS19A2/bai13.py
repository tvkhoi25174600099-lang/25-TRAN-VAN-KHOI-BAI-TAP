n = int(input())
don_vi = True

for i in range(n):
    for j in range(n):
        x = int(input())
        if (i == j and x != 1) or (i != j and x != 0):
            don_vi = False

print(don_vi)
