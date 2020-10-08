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

# 入力値が大きいとランタイムエラーになるのであらかじめ数値をセットする
# 400年周期であることを利用
# 400の倍数年未来に飛ぶ
days400y = 365 * 400 + int(400 / 4) - int(400 / 100) + int(400 / 400)
day_cnt += int((year - y) / 400) * days400y
y = int(((year - y) // 400) * 400) +y


# 一日ずつ進める
while True:
    if y == year and m == month and d == day:
        break
    y, m, d = next_date(y, m, d)
    day_cnt += 1

week_day_list = ["水", "木", "金", "土", "日", "月", "火"]
week_day = day_cnt % 7

print(week_day_list[week_day] + "曜日")

# 別解
# year, month, day = map(int, input().split())
#
# week_dict = {"0": "日曜日", "1": "月曜日", "2": "火曜日", "3": "水曜日", "4": "木曜日", "5": "金曜日", "6": "土曜日"}
#
# # ツェラーの公式を使って算出
# # 1月と2月は前年の13月14月として計算する。
# if month == 1 or month == 2:
#     year -= 1
#     month += 12
# week_day = (31 + 28 + 365*(year-1) + int(year/4) - int(year/100) + int(year/400) + int(306*(month +1) / 10) -122 + day) % 7
#
#
# print(week_dict[str(week_day)])
