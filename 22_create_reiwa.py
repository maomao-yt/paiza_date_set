N = int(input())

word = []
for i in range(N):
    word.append(input())

cnt = 0
ans_list = []
for i in range(N):
    for j in range(N):
        ans = word[i] + word[j]
        ans_list.append(ans)
        cnt += 1
        if cnt <= 1000:
            print(ans)
if "令和" in ans_list:
    print("Nice")
else:
    print("Bad")