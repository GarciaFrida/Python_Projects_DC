#user_entries = int(input("Please enter a number:\n"))
new_user_list = []
#new_user_list.append(user_entries)
#print(new_user_list)
result = 0
try:
    user_entries = int(input("Please enter a number:\n"))
except ValueError:
    print("please enter a number")


while len(new_user_list) < 6:
    new_user_list.append(user_entries)
    print(new_user_list)
    user_entries = int(input("Please enter a number:\n"))
  
    


 




