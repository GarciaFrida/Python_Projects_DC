#Create a program that will ask for a username and then a password.
#If the username or password length is less than 6 charecters give a too short message.
#if the username or password length is greater than 12 charecters give a too long message
#Have the user confirm the password in again.
#If the passwords match give a sucess message
#if the passwords do not match give a mismatch message
#If the password is only numbers give a message that says it cannot be a number.
#challange have only one print statement in the whole program.



user_name = input("""
Please Enter Username: 
""")

password = input("""
Please Enter Password: 
""")

if len(user_name) < 6 and len(password) < 6:
    print("Too Short")

elif len(user_name) > 6 and len(password) > 6:
    print("Too Long")


print("""
Please Confirm Password:
""")

password_confirmation = input()


if password_confirmation == password:
    print("Success")

else:
    print("Please try again")


