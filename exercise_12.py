cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
#cheese += 'Oke'
cheese += ['Oke']
print(cheese)
# missing the square brackets and so each element of the string was added to the list
cheese.extend(['melted', 'grated'])
print(cheese)

tup = "Hello"
print(len(tup))

tup = "Hello",
print(len(tup))

# the first tup is a string with 5 elements, the second tup is a tuple with one element