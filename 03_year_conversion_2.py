y, m, d = input().split()
year =int(y)
# 月、日が1桁の場合0パディングする。
if len(m) == 1:
    m = "0" + m
if len(d) == 1:
    d = "0" + d

# 年、月、日を結合しint型に変換
date = int(y + m + d)

# 和暦の判別
if date < 19120730:
    year -= 1867
    if year == 1:
        wareki = "明治元年"
    else:
        wareki = "明治"+str(year)+"年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19120730 and date < 19261225:
    year -= 1911
    if year == 1:
        wareki = "大正元年"
    else:
        wareki = "大正"+str(year)+"年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19261225 and date < 19890108:
    year -= 1925
    if year == 1:
        wareki = "昭和元年"
    else:
        wareki = "昭和"+str(year)+"年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19890108 and date < 20190431:
    year -= 1988
    if year == 1:
        wareki = "平成元年"
    else:
        wareki = "平成"+str(year)+"年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

else:
    year -= 2018
    if year == 1:
        wareki ="令和元年"
    else:
        wareki = "令和"+str(year)+"年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")
