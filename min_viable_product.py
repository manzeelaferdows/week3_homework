import random

help(random)

lotto_numbers = []
for i in range(0, 6):
    number = random.randint(1, 50)
    while number in lotto_numbers:
        number = random.randint(1, 50)
    lotto_numbers.append(number)
print(lotto_numbers)

# use a while loop (not a for loop) and make a set containing the lotto numbers
# the data collection set will ensure no repetitions are in the lottery numbers
