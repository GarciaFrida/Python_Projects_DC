
#bill_amount = float(input())

try:
    bill_amount = float(input("Pleas enter your bill amount:\n"))
except ValueError:
    print("Please enter a valid number")

service_quality = input("Please rate your service (good, fair, bad):\n")
tip = 0
if service_quality == "Good":
    tip = bill_amount*0.2
elif service_quality == "Fair":
    tip = bill_amount*.15
elif service_quality == "Bad":
    tip = bill_amount*.10
else:
    print(input("Please specify an amount:\n"))

total_amount = tip + bill_amount

print("Your total amount plus tip is: %s" % total_amount)

split_check = input("Would you like to split the check?\n")

print(split_check)

how_many_ways =  
