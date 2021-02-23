import random

help(random)

lotto_numbers = set()
while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 50))
print(lotto_numbers)

# use a while loop (not a for loop) and make a set containing the lotto numbers
# the data collection set will ensure no repetitions are in the lottery numbers
