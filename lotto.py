import random
#print(help(random))
lucky_numbers = input('please type in your 6 lucky numbers')

lotto_numbers = []
for i in range(0, 6):
    number = random.randint(1, 50)
    while number in lotto_numbers:
        number = random.randint(1, 50)
    lotto_numbers.append(number)
print(lotto_numbers)
if lotto_numbers == lucky_numbers:
    print("You win as the lottery numbers {} matches your lucky numbers{}".format(lotto_numbers, lucky_numbers))
else:
    print("Better luck next time. The lottery numbers {} didn't match your lucky numbers{}".format(lotto_numbers,
                                                                                                   lucky_numbers))

