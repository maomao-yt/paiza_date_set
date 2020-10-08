# 閏年判定
def is_leap(year):
    if year % 400 == 0 or( year %  100 != 0 and year % 4 == 0):
        return True
# 最終日を求める
def last_day(year, month):
    if month == 2:
        # 閏年かどうか
        if is_leap(year):
            day =29
        else:
            day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    else:
        day = 31
    return day

# 次の日を求める
def next_date(year, month, day):
    day += 1
    if day > last_day(year, month):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return year, month, day


year, month, day = map(int, input().split())
# 基準日
y, m, d = 1800, 1, 1
day_cnt = 0
while True:
    if y == year and m == month and d == day:
        break
    y, m, d = next_date(y, m, d)
    day_cnt += 1


week_day_list = ["水","木","金","土","日","月","火"]
week_day = day_cnt % 7

print(week_day_list[week_day]+"曜日")



# 別解
# import datetime
#
# year, month, day = map(int, input().split())
# week_dict = {"Mon": "月曜日", "Tue": "火曜日", "Wed": "水曜日", "Thu": "木曜日", "Fri": "金曜日", "Sat": "土曜日", "Sun": "日曜日"}
#
# dt = datetime.datetime(year, month, day)
# week_day = dt.strftime('%a')
#
# print(week_dict[week_day])
