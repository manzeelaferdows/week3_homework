import random

#print(help(random))
lucky_numbers = input('Please type in your 6 lucky numbers between 1-50 (with a space between each number) : ')
lucky_numbers_list = []
for number in lucky_numbers.split():
    lucky_numbers_list.append(int(number))

lotto_numbers = []
for i in range(0, 6):
    numbers = random.randint(1, 51)
    while numbers in lotto_numbers:
        numbers = random.randint(1, 51)
    lotto_numbers.append(numbers)

lotto_numbers.sort()
lucky_numbers_list.sort()
if lotto_numbers == lucky_numbers_list:
    print("You win as the lottery numbers {} matches your lucky numbers{}".format(lotto_numbers, lucky_numbers_list))
else:
    print("Better luck next time. The lottery numbers {} didn't match your lucky numbers{}".format(lotto_numbers, lucky_numbers_list))
