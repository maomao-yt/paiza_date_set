y, m, d = input().split()

# 月、日が1桁の場合0パディングする。
if len(m) == 1:
    m = "0" + m
if len(d) == 1:
    d = "0" + d

# 年、月、日を結合しint型に変換
date = int(y + m + d)

# 和暦の判別
if date < 19120730:
    wareki = "明治年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19120730 and date < 19261225:
    wareki = "大正年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19261225 and date < 19890108:
    wareki = "昭和年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

elif date >= 19890108 and date < 20190431:
    wareki = "平成年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")

else:
    wareki = "令和年"
    print(wareki + str(int(m)) + "月" + str(int(d)) + "日")
