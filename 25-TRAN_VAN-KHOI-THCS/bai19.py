n = int(input())
d = {}

for i in range(n):
    ten = input()
    diem = int(input())
    if diem not in d:
        d[diem] = []
    d[diem].append(ten)

print(d)
