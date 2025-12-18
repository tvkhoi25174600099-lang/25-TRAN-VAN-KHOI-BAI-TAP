s = input()

so_tu = 0
so_ky_tu = 0
ky_tu_dac_biet = 0
trong_tu = False

for ch in s:
    so_ky_tu += 1
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
        trong_tu = True
    elif ch == ' ':
        if trong_tu:
            so_tu += 1
            trong_tu = False
    else:
        ky_tu_dac_biet += 1

if trong_tu:
    so_tu += 1

print("So tu:", so_tu)
print("So ky tu:", so_ky_tu)
print("Ky tu dac biet:", ky_tu_dac_biet)