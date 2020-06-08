import random

random_coin = random.randint(1, 10)
coin_flip = int(input("Flip a coin(Pick a number from 1 - 10)? "))
guess_again = int(input("Do you wanna guess again? "))

while random_coin != coin_flip:
    if coin_flip >= 5:
        print("Heads")
    elif coing_flip <= 10:
        print("Tails")
        guess_again = int(input("Do you wanna guess again? "))
    else:
        exit()