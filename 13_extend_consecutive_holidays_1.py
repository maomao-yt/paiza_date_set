N, L = map(int, input().split())
days = [int(i) for i in input().split()]


def holidays_num(start):
    one = 0
    zero = 0

    while start + one + zero < N:
        if days[start + one + zero] == 1:
            one += 1
        else:
            # ゼロの回数が有給取得可能数と同じならループを抜ける
            if zero == L:
                break
            zero += 1
    return one + zero


result = 0
ans = 0
# スタート位置を１つずつずらす
for start in range(N):
    result = holidays_num(start)
    ans = max(ans, result)
print(ans)
