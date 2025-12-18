n = int(input())
t = ()

for i in range(n):
    t += (int(input()),)

chan = ()
le = ()
tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan += (x,)
        tong_chan += x
    else:
        le += (x,)
        tong_le += x

print(chan, tong_chan)
print(le, tong_le)
