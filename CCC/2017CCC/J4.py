number_of_minutes = input()
start_hour = "12"
start_min = "00"

for i in range(number_of_minutes):
    if int(start_min) <= 58:
        if start_min[0] == "0":
            new = int(start_min[1])
            new += 1
            start_min[1] = str(new)
        else:
            start_min += 1
    elif start_min == 59:
        start_min = 00
        if start_hour == 12:
            start_hour = 1
        else:
            start_hour += 1

    print start_hour + ":" + start_min



