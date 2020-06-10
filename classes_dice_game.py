# Create a program (using using only a single class) that creates a dice rolling system for a d6, d12, d20.
# Have the user choose one of the 3 dice and roll it. 
# Have each dice keep a record of how many times it was rolled and what was rolled.
# Have the user be able to request the average roll for a single dice.
# (Challange) Create a Cheat d20 dice that has a cheat_roll function that will ask for a target number and get within two of that number. However it can only be used once every 10 rolls. (this can be a subclass)
# (Extra Challange) Allow a user to 'create' their own dice of any size, and be able to use it in the program.
# (Extra Extra Challange) have a menu for each dice to have options like "show rolls, show averages,reset roll count.
import random


# choice_of = input("Pick a Dice (d3, d6, or d20): ")
def die(choice):
        choice = " "
        if choice == "d6" or choice == "D6":
            sides = random.randint(1, 6)
        elif choice == "d12" or choice == "D12":
            sides = random.randint(1, 12)
        elif choice == "d20" or choice == "D20":
            sides = random.randint(1, 20)
        return(sides)

print(die("D6"))


# class Dice():


#     def __init__(self, sides):
#         self.sides = sides
        
#     def die(self, choice):
#         choice = "Pick a Dice (d6, d12, or d20)"
#         if choice == "d6" or choice == "D6":
#             self.sides = random.randint(1, 6)
#         elif choice == "d12" or choice == "D12":
#             self.sides = random.randint(1, 12)
#         elif choice == "d20" or choice == "D20":
#             self.sides = random.randint(1, 20)



# class Character():

#     def __init__(self, name, position, speed=10, health=100, attack_power=5):
#         print("A character was created")
#         self.name = name
#         self.health = health
#         self.speed = speed
#         self.position = position
#         self.attack_power = attack_power


#     def attack(self, char):
#         char.health -= self.attack_power

#     def move(self, dir):
#         if dir == "right":
#             self.positions["x"] += self.peed
#         elif dir == "left":
#             self.position["x"] -= self.speed
#         elif dir == "up":
#             self.position["y"] -= self.speed
#         elif dir == "down":
#             self.position["y"] += self.speed

# class Player(Character):
#     def heal(self):
#         self.health += 25

# class Enemy(Character):
#     def __init__(self, name, position):
#         super().__init__(name,position)
#         self.health = 50
#         self.speed = 40
#         print("Enemy has entered the chat")
#         # self.name = name
#         # self.health = 50
#         # self.speed = 40
#         # self.position = position
#         # self.attack_power = 68

#     def roll(self):
#         self.position["x"] -= 25


# enemy1 = Enemy("Enemy", {"x":1, "y":100})
# player1 = Player("Bob", {"x":10, "y":200}, 140, 1000)

# while player1.health > 300:
#     enemy1.attack(player1)
#     print(player1.health)

# player1.attack(enemy1)
# print(enemy1.health)



    