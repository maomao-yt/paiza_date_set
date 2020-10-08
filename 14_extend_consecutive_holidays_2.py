"""
使いどころ
２つの数値や文字
同じ要素の数が連続で出てくる場合
"""
N, L = map(int, input().split())
days = [int(i) for i in input().split()]

result = 0
one = 0
zero = 0
left = 0
ans = 0
# N<=100,000
for i in range(N):
    if days[i] == 1:
        one += 1
    else:
        # zero1カウント＝有給を1日とる
        zero += 1
        while zero > L: # 有給を取りすぎた場合
            if days[left] == 1:
                one -= 1
            else:
                zero -= 1
            left += 1
    ans = max(ans,one + zero)
print(ans)
