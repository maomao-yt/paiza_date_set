# 閏年判定
def is_leap(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True

# 最終日を求める
def last_day(year, month):
    if month == 12:
        # 閏年かどうか
        if is_leap(year):
            day = 31
        else:
            day =30
    else:
        day = 30
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

# 0年1月1日（木）から数えてyear年month月day日が何日先か
year, month, day = map(int, input().split())
# 基準日
y, m, d = 0, 1, 1
day_cnt = 0

# 入力値が大きいとランタイムエラーになるのであらかじめ数値をセットする
# 400年周期であることを利用
# 400の倍数年未来に飛ぶ
days400y = 360 * 400 + int(400 / 4) - int(400 / 100) + int(400 / 400)
day_cnt += int((year - y) / 400) * days400y
y = int(((year - y) // 400) * 400) +y


# 一日ずつ進める
while True:
    if y == year and m == month and d == day:
        break
    y, m, d = next_date(y, m, d)
    day_cnt += 1

week_day_list = ["木", "金", "土", "日", "月", "火", "水"]
week_day = day_cnt % 7

print(week_day_list[week_day] + "曜日")