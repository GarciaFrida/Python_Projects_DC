#Create a program that asks for a number between 10 - 101. 
#If the user enters anything that is not a number, or is less than 10 or greater than 101 throw some sort of insult.
#If the number is 42 print a very positive message.
#If the number -1 disregard the first point and print a message about being a smart person.
#Any other print a message that includes the number given.
#Create a program that ask for 2 numbers and then divides the first number from the second number.
#Handle any possible errors without using any 'if'.
#If the result is a valid option, print "The result is X" where X is the value.
#Otherwise give an error that describes the issue.
#(challange) Still without using if. Let the user know which value is causing and exemption.
#(Extra Challange) Still without using ifs, If the first or second value is not a valid integer, have the program keep asking UNTIL the user supplies a valid integer. (think about the bolded word)


#Here I'm going to ask the user for the input
guess_number = input("Pick a number from 10 - 101: ")
try:
    number = int(number)
except ValueError:
    print("You don't know anything")
    exit()
    
if guess_number < 10 or guess_number > 101:
    print("You're dumb")
elif guess_number == 42:
    print("You're so bright!")
elif guess_number == -1:
    print("You're still the smartest person I know")
else: 
    print("Your guess was incorrect, the number is 42")

ask_for_one = int(input("Pick a number: "))
ask_for_two = int(input("Pick another number: "))


result_for_two = ask_for_one/ask_for_two
try:
    print("The result is %s" % result_for_two)
except ZeroDivisionError:
    print("you suck")





