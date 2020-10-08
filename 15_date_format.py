date = input().split("/")

try:
    flag = False
    if len(date) != 3:
        print("No")
    elif len(date[0]) != 4:
        print("No")
    elif not (int(date[1]) in range(1, 13)):
        print("No")
    elif not (int(date[2]) in range(1, 32)):
        print("No")
    else:
        flag = True
except:
    print("No")
else:
    if flag:
        print("Yes")