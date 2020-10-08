date = input().split("/")

if len(date[0])==4:
    date[0]="YYYY"
    if int(date[1]) in range(1,13):
        if int(date[2]) in range(1,13):
            print("many answers")
        elif int(date[2]) in range(13,32):
            date[1] ="MM"
            date[2] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    elif int(date[2]) in range(1,13):
        if int(date[1]) in range(13,32):
            date[2] ="MM"
            date[1] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    else:
        print("no answer")
elif len(date[1])==4:
    date[1] = "YYYY"
    if int(date[0]) in range(1,13):
        if int(date[2]) in range(1,13):
            print("many answers")
        elif int(date[2]) in range(13,32):
            date[0] ="MM"
            date[2] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    elif int(date[2]) in range(1,13):
        if int(date[0]) in range(13,32):
            date[2] ="MM"
            date[0] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    else:
        print("no answer")
elif len(date[2])==4:
    date[2] = "YYYY"
    if int(date[0]) in range(1,13):
        if int(date[1]) in range(1,13):
            print("many answers")
        elif int(date[1]) in range(13,32):
            date[0] ="MM"
            date[1] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    elif int(date[1]) in range(1,13):
        if int(date[0]) in range(13,32):
            date[1] ="MM"
            date[0] ="DD"
            print("/".join(date))
        else:
            print("no answer")
    else:
        print("no answer")
else:
    print("no answer")