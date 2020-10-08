line = input()

ans = 0
for i in range(len(line)-1):
    word =line[i:i+2]
    if word =="令和":
        ans += 1
print(ans)