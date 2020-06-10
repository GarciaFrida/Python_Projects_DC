# class Dogs():
#     def how_many_dogs_is_enough_dogs(start_count, end_count, breed_rating):
#         print(self)
#         results = start_count - end_count
#         if start_count < end_count:
#             print("Think of all the dogs out there, needs to be a bigger num")
#         else:
#             return results


# dog_breed = Dogs()

# breed_rating= {
#     "Giant Schnauzer" : 10,
#     "Great Dane" : 10,
#     "Giant Poodle" : 8,
#     "Pitbull" : 10,
#     "Chihuahua" : -1
#     }

# Dogs.how_many_dogs_is_enough_dogs(45, 32, "Giant Schnauzer")




class Character():

    def __init__(self, name, position, speed=10, health=100, attack_power=5):
        print("A character was created")
        self.name = name
        self.health = health
        self.speed = speed
        self.position = position
        self.attack_power = attack_power


    def attack(self, char):
        char.health -= self.attack_power

    def move(self, dir):
        if dir == "right":
            self.positions["x"] += self.peed
        elif dir == "left":
            self.position["x"] -= self.speed
        elif dir == "up":
            self.position["y"] -= self.speed
        elif dir == "down":
            self.position["y"] += self.speed

class Player(Character):
    def heal(self):
        self.health += 25

class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.health = 50
        self.speed = 40
        print("Enemy has entered the chat")
        # self.name = name
        # self.health = 50
        # self.speed = 40
        # self.position = position
        # self.attack_power = 68

    def roll(self):
        self.position["x"] -= 25


enemy1 = Enemy("Enemy", {"x":1, "y":100})
player1 = Player("Bob", {"x":10, "y":200}, 140, 1000)

while player1.health > 300:
    enemy1.attack(player1)
    print(player1.health)

player1.attack(enemy1)
print(enemy1.health)

 


