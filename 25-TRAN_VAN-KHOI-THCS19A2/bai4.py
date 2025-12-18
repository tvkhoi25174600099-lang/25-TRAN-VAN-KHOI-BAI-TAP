n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

max2 = None
for x in a:
    if x != max1:
        if max2 is None or x > max2:
            max2 = x

print(max2)
