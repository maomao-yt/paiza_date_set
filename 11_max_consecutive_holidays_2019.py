year, month, day = 2019, 1, 1
week_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day_cnt = 2

# 2019年の国民の祝日をリストに格納
holiday = ["1 1", "1 14", "2 11", "3 21", "4 29", "4 30", "5 1", "5 2", "5 3", "5 4", "5 5", "5 6",
           "7 15", "8 11", "8 12", "9 16", "9 23", "10 14", "10 22", "11 3", "11 4", "11 23"]


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


consecutive_holidays_num = 0
holiday_cnt = 0
while year != 2020:

    if f"{month} {day}" in holiday or week_day[day_cnt % 7] == "SUN" or week_day[day_cnt % 7] == "SAT":
        holiday_cnt += 1
        consecutive_holidays_num = max(consecutive_holidays_num, holiday_cnt)
    else:
        holiday_cnt = 0
    year, month, day = next_date(year, month, day)
    day_cnt += 1

print(consecutive_holidays_num)
