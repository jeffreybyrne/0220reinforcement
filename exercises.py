# Exercise 1
# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.
#
# Test it to make sure it works.

def sum_odds(list):
    sum = 0
    for num in range(0,len(list)):
        if list[num] % 2 == 1:
            sum +=  list[num]
    return sum

my_list = [400,2,67,42,3,221,1332,957,93536,120412]

print(sum_odds(my_list))

# Exercise 2
# Pick three names and store them in a list.
#
# Prompt the user to enter their name. If their name is one of the names in the list, display a greeting message that
# includes their name. If their name isn't in the list, display "Who goes there?"
name_list = ['Jeff','Natalie','Sean']

print("What is your name?")
name = input()
if name in name_list:
    print("Welcome to the club!")
else:
    print("Who goes there?")
