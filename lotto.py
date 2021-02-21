import random
#print(help(random))
lucky_number = input('please type in your 6 lucky numbers')
random.randint(1,6)
lottonumbers = []
for i in range(0,6):
    numbers = random.randint(1,50)
    while numbers in lottonumbers:
        numbers = random.randint(1,50)
    lottonumbers.append(numbers)
print(lottonumbers)
if lottonumbers==lucky_number:
    print("You're the winner")
else:
    print("Better luck next time")

