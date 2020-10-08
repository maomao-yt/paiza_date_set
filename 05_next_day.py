year, month, day = map(int, input().split())
day += 1

if month == 2 and (day == 29 or day == 30):
    # 閏年の判定
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0 and day == 30:
                day -= 29
                month += 1
            else:
                day -= 28
                month += 1
        elif day == 30:
            day -= 29
            month += 1
    else:
        day -= 28
        month += 1

# 2月以外の月の判定
elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 31:
    day -= 30
    month += 1
elif day == 32:
    day -= 31
    month += 1
    if month == 13:
        month -= 12
        year += 1

print(year, month, day)
