y, m = map(int, input().split())
# 基準日
year, month, day = 1800, 1, 1
# 曜日は0,1,2,3,4,5,6で管理。0を日曜日とする
day_cnt = 3  # 基準日は水曜日


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


# 入力した年月になるまでループ
while True:
    if year == y and month == m:
        break
    year, month, day = next_date(year, month, day)
    day_cnt += 1

calender = []
sub_calender = ["  "] * 7
cnt = 0
while True:
    year, month, day = next_date(year, month, day)
    cnt += 1
    # 日にちを文字列に変換
    if len(str(cnt)) == 1:
        ans = " " + str(cnt)
    else:
        ans = str(cnt)
    sub_calender[day_cnt % 7] = ans
    if month != m:
        calender.append(sub_calender)
        # カレンダーが6行未満だったら
        while len(calender) != 6:
            sub_calender = ["  "] * 7
            calender.append(sub_calender)
        break
    if day_cnt % 7 == 6:  # 土曜日だったら次の週に移る
        calender.append(sub_calender)
        sub_calender = ["  "] * 7
    day_cnt += 1

for week in calender:
    week = [str(i) for i in week]
    week = " ".join(week)
    print(week)
