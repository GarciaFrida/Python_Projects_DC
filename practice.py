
# days_of_week = {
#     "Monday" : "Lunes",
#     "Tuesday" : "Martes",
#     "Wendesday" : "Miercoles",
#     "Thursday" : "Jueves",
#     "Friday" : "Viernes",
# }

# # print(days_of_week)

# list_of_my_friends = {
#     "Arlene" : "21",
#     "Mario" : 27,
#     "Kathy" : [32, 45],
#     "Chip" : { 
#         "Friends" : 20,
#         "Sister" : 15,
#         "Junior League" : ["Hail", "Payne"]
#     }
        
# }

# list_of_my_friends["Chip"]["Family"] = ["Father", "Mother"]

# list_of_my_friends["Chip"]["Family"] = "Sister"



# print(list_of_my_friends)

# dictionaries are accessed by keys 

# print(list_of_my_friends["Chip"])

# del list_of_my_friends["Chip"]
# # print(list_of_my_friends)

# if "Chip" in list_of_my_friends:
#     print("Don't hang out with teens")
# else:
#     print("You safe bby")

# for key in list_of_my_friends:
#     print(list_of_my_friends[key])
#     # print(key)

# my_best_friends = list_of_my_friends["Chip"]
# my_best_friends["Nisha"] = "Old Besties"
# # print(my_best_friends)

# print(list_of_my_friends)



# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob' : '857-384-1234',
#     'Elizabeth' : '484-584-2923'
# }

# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'

# print(phonebook_dict)

ramit = {
    'name' : 'Ramit',
    'email' : 'ramit@gmail.com',
    'interests' : ['movies', 'tennis'],
    'friends' : [
        {
            'name' : 'Jasmine',
            'email' : 'jasmine@yahoo.com',
            'interests' : ['photography', 'tennis']
        },
        {
            'name' : 'Jan',
            'email' : 'jan@hotmail.com',
            'interests' : ['movies', 'tv']
        }
    ]
}

# email_for_ramit = ramit['email']
# print(email_for_ramit)

# interests_for_ramit = ramit['interests']
# print(interests_for_ramit)

# email_for_jasmine = ramit['friends'][0]['email']
# print(email_for_jasmine)

# interests_for_jan = ramit['friends'][1]['interests'][1]
# print(interests_for_jan)

letter_histogram = 