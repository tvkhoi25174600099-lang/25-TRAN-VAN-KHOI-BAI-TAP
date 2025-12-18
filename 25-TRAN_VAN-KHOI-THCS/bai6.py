n = int(input())
tong_chan = 0
tong_le = 0

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print(tong_chan, tong_le)
