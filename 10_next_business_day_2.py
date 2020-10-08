M, D, d = input().split()
M, D = int(M), int(D)
week_day =["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
list_num = 0

# 2019年の国民の祝日をリストに格納
holiday = ["1月1日","1月14日","2月11日","3月21日","4月29日","4月30日","5月1日","5月2日","5月3日","5月4日","5月5日","5月6日",
           "7月15日","8月11日","8月12日","9月16日","9月23日","10月14日","10月22日","11月3日","11月4日","11月23日"]


# dからweek_dayのリスト番号を取得
for i,day in enumerate(week_day):
    if day == d:
        list_num = i
        break

D += 1
list_num += 1
# 翌営業日になるまでループ
while True:
    if d == "FRI":
        D += 2
        list_num = 1
    elif d == "SAT":
        D += 1
        list_num = 1
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

    next_day =str(M) + "月" + str(D) + "日"
    # 翌営業日が国民の祝日かどうか判定
    if next_day in holiday:
        D += 1
        list_num += 1
        d = week_day[list_num%7]
    else:
        break

print(next_day)

