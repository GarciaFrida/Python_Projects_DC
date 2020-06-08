day = int(input("What day of the week is it today (0-6)? "))

zero = "Sunday"
work_or_sleep = "sleep in"
sleep_or_work = "go to work"
one = "Monday"
two = "Tuesday"
three = "Wednesday"
four = "Thursday"
five = "Friday"
six = "Saturday"

if day == 0:
    print("It is %s,  %s " % (zero, work_or_sleep))
elif day == 1:
    print("It is %s, %s " % (one, sleep_or_work))
elif day == 2:
    print("It is %s, %s " % (two, sleep_or_work))
elif day == 3:
    print("It is %s, %s " % t(hree, sleep_or_work))
elif day == 4:
    print("It is %s, %s " % (four, sleep_or_work))
elif day == 5:
    print("It is %s, %s " % (five, sleep_or_work))
elif day == 6:
    print("It is %s, %s " % (six, work_or_sleep))
else:
    print("Please input a day")