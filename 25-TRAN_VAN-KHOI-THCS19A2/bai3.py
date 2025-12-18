s = input()
kq = ""
truoc_la_space = False

for ch in s:
    if ch != ' ':
        kq += ch
        truoc_la_space = False
    else:
        if not truoc_la_space:
            kq += ch
            truoc_la_space = True

print(kq)
