
welcome_note = """
Welcome to the Python recipe book. \n
"""
print(welcome_note)
user_input = input("""
What recipe would you like to see (recipe-1, recipe-2, recipe-3): ?\n 
""")
# try:
#     if welcome_note == recipe-1:
        

# except ValueError:
#     print("Please enter in the format recipe-1, recipe-2, recipe-3")
    



recipe_list = {
    'recipe-1' : {
        'name' : 'Sandwich',
        'ingredients' : [
            {
                'name': 'Ham or Turkey',
                'amount' : 'as much as you like'
            }, {
                'name' : 'Bread, any kind',
                'amount' : 'two pieces, spread mayo on both'
            }, {
                'name' : 'cheese, any kind',
                'amount' : 'as much as you like'
            }
        ]
    },
    'recipe-2' : {
        'name' : 'Tuna',
        'ingredients' : [
            {
                'name' : 'Tuna (preferably in a can',
                'amount' : 'about one to two cans'
            }, {
                'name' : 'Mayo',
                'amount' : 'any kind, preferably vegan'
            }, {
                'name' : 'Crackers',
                'amount' : 'As many as you would like'
            }
        ]
    },
    'recipe-3' : {
        'name' : 'Adult Lunchables',
        'ingredients' : [
            {
                'name' : 'Crackers (any kind that you like',
                'amount' : 'as many as you want'
            }, {
                'name' : 'Ham or Turkey',
                'amount' : 'as much you would like, but it has to match the amount of crackers'
            }, {
                'name' : 'Cheese (any kinds, munster is preferable',
                'amount' : 'as much as you would like but it has to match the cracker amount'
            }
        ]
    }
}

recipe_one = recipe_list['recipe-1']
recipe_two = recipe_list['recipe-2']
recipe_three = recipe_list['recipe-3']

# back_to_menu = int(input("""
# Would you like to go back to the main menu?\n (1-yes, 2-no)
# """))

for recipe_one in recipe_list:
    if user_input == 'recipe-1':
        print(recipe_list['recipe-1']['name'])
        print(recipe_list['recipe-1']['ingredients'][0])
        print(recipe_list['recipe-1']['ingredients'][1])
        print(recipe_list['recipe-1']['ingredients'][2])
        exit()

     
for recipe_two in recipe_list:
    if user_input == 'recipe-2':
        print(recipe_list['recipe-2']['name'])
        print(recipe_list['recipe-2']['ingredients'][0])
        print(recipe_list['recipe-2']['ingredients'][1])
        print(recipe_list['recipe-2']['ingredients'][2])
        exit()

for recipe_three in recipe_list:
    if user_input == 'recipe-3':
        print(recipe_list['recipe-3']['name'])
        print(recipe_list['recipe-3']['ingredients'][0])
        print(recipe_list['recipe-3']['ingredients'][1])
        print(recipe_list['recipe-3']['ingredients'][2])
        exit()


