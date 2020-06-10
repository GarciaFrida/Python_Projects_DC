

def mad_lib(name, subject):
    try:
        print("%s's favorite subject is %s" % (name, subject))
    except TypeError:
        print('You need to insert a subject')


print(mad_lib('Jen','Math'))


#celsius to Fahrenheit

def c_to_f(c):
    f = (c * 9/5) + 32
    return f

print(c_to_f(23))

def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)


# is_even(4)


# only_evens

# only_evens = []

def only_evens(is_even):
    
    return only_evens

print(only_evens([11, 93, 34]))


#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
      return lst1
  elif len(lst1) == len(lst2):
      return lst1[-1]
  else:
      return lst2

    
    
    

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


def smallest(lst):
    while len(lst) > 5:
