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
