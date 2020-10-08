import datetime
import math


# 閏年判定
def is_leap(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True


# 最終日を求める
def last_day(year, month):
    if month == 2:
        # 閏年かどうか
        if is_leap(year):
            day = 29
        else:
            day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    else:
        day = 31
    return day

X = int(input())
# カレンダーの周期性
# 400年の周期と7日の周期をかける
week_cnt = [0, 0, 0, 0, 0]
all_month = 0
start_year = 1800
end_year = 1800 + 400
for year in range(start_year, end_year):
    for month in range(1, 13):
        day = last_day(year, month)
        dt = datetime.datetime(year, month, day)
        week = dt.strftime('%a')  # 曜日を算出
        if week == "Mon":
            week_cnt[0] += 1
        elif week == "Tue":
            week_cnt[1] += 1
        elif week == "Wed":
            week_cnt[2] += 1
        elif week == "Thu":
            week_cnt[3] += 1
        elif week == "Fri"or week=="Sat" or week=="Sun":
            week_cnt[4] += 1
        all_month += 1

ans = (week_cnt[(X-1) % 5] / all_month)
print(math.floor(ans * 1000000) / 1000000)  # 欲しい桁数までかけて、math.floorで切り捨てを行い、また同じ数で割る
