year ,month = map(int,input().split())

if month == 2:
    # 閏年の判定
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 ==0:
                print(29)
            else:
                print(28)
        else:
            print(29)
    else:
        print(28)

# 2月以外の月の判定
elif month == 4 or month ==6 or month == 9 or month == 11:
    print(30)

else:
    print(31)