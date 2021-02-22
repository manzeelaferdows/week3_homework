import random
#print(help(random))
lucky_numbers = input('please type in your 6 lucky numbers')
random.randint(1, 6)
lotto_numbers = []
for i in range(0, 6):
    numbers = random.randint(1, 50)
    while numbers in lotto_numbers:
        numbers = random.randint(1, 50)
    lotto_numbers.append(numbers)
print(lotto_numbers)
if lotto_numbers == lucky_numbers:
    print("You're the winner")
else:
    print("Better luck next time")
#Do we need to convert lucky numbers into a list?
