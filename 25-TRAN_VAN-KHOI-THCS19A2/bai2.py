s = input()
n = int(input())

tu = ""
for ch in s:
    if ch != ' ':
        tu += ch
    else:
        if len(tu) > n:
            print(tu)
        tu = ""

if len(tu) > n:
    print(tu)
