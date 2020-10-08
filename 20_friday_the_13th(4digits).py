import datetime
import math

# カレンダーの周期性
# 400年の周期と7日の周期をかける
fri = 0
all_month = 0
start_year = 1800
end_year = 1800 + 400 * 7
for year in range(start_year, end_year):
    for month in range(1, 13):
        dt = datetime.datetime(year, month, 13)
        week = dt.strftime('%a')  # 曜日を算出
        if week == "Fri":
            fri += 1
        all_month += 1
ans = (fri / all_month)
print(math.floor(ans * 10000) / 10000)  # 欲しい桁数までかけて、math.floorで切り捨てを行い、また同じ数で割る
