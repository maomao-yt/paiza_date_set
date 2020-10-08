import random
import datetime
import math

fri = 0
for i in range(100000):
    year = random.randint(1800, 3000)  # 適当に1800年から3000年を抽出
    month = random.randint(1, 12)  # 適当に1月から12月を抽出
    dt = datetime.datetime(year, month, 13)
    week = dt.strftime('%a')  # 曜日を算出
    if week == "Fri":
        fri += 1

ans = (fri / 100000)
print(math.floor(ans * 100) / 100)  # 欲しい桁数までかけて、math.floorで切り捨てを行い、また同じ数で割る
