"""
The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.
"""
import random

my_randoms = random.sample(range(1, 32), 23)
print(my_randoms)


def has_duplicates():
    count = 0
    for i in range(0, len(my_randoms) - 1):
        for j in range(i + 1, len(my_randoms)):

            if my_randoms[i] == my_randoms[j] and j != 0:
                my_randoms[count] = 0
                return True
            count = count + 1
    return False


cont = 0
for i in my_randoms:
    if (has_duplicates() == True):
        cont = cont + 1
print("Probability is " + str(cont) + " in 23")
