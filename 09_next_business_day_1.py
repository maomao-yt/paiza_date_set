M, D, d = input().split()
M, D = int(M), int(D)

D += 1
if d == "FRI":
    D += 2
elif d == "SAT":
    D += 1

if M == 2 and D > 28:
    D -= 28
    M += 1

# 2月以外の月の判定
elif (M == 4 or M == 6 or M == 9 or M == 11) and D > 30:
    D -= 30
    M += 1
elif D > 31:
    D -= 31
    M += 1
    if M > 12:
        M = 1

print(str(M) + "月" + str(D) + "日")
