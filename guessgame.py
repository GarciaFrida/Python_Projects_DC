import random

my_random_number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")

user_guess = int(input("What's the number? "))

while user_guess != my_random_number:
    if user_guess > 10:
        print("%s is too high." % user_guess)
    elif user_guess < 0:
        print("%s is too low." % user_guess)
    #print("Nope, try again.")
    user_guess = int(input("What's the number? "))
else:
    print("Yes! You win!")
