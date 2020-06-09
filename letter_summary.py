word = input("""
Please enter a word:
""")
word_list = {}
for letter in word_list:
    if(letter in word_list):
        word_list[letter] += 1
    else: 
        word_list[letter] = 1


print(word_list)

