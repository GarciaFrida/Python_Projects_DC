#Create a program that asks for a name and if the name is your name print "You May Enter", otherwise print "Get Out"
#Anything printed must be a variable.
#Create a Program that ask for an age if the age is older than 21 print "You may enter" otherwise print "Get Out"
#Test it with a letter instead of a number... and then speak up in chat what happens.

print("Please Enter Your Name:")
user_name = "Frida"
name_given = input()


if name_given == user_name:
    print("You May Enter")

else:
    print("Get Out")


print("Please Enter Your Age:")

older_than_twentyone = 21
age_of_user = int(input())


if age_of_user >= older_than_twentyone:
    print("Welcome!")
else:
    print("Get out!")