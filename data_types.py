str = 'Norwegian Blue', "Mr Khan's Bike"
list = ['cheddar', ['Camembert', 'Brie'], 'Stilton', 'Brie', 'Brie']
tuples = (47, 'spam', 'Major', 638, 'Ovine Aviation')
tuples2 = (36, 29, 63)
set = {'cheeseburger', 'icecream', 'chicken nuggets'}
dict = {'Totness': 'Barber', 'BritishColumbia': 'Lumberjack'}

print(len(list))
print(min(tuples2))
print(max(tuples2))
print(sum(tuples2))

a = 'Mash Potato'
b = 'Gravy'

print(a, b)
a, b = b, a
print(a, b)

Gouda, Edam, Caithness = range(3)
print(range)

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
Belgium2 = Belgium*2
print(Belgium2)

thing = 'Hello'
print(type(thing))
thing = ('Hello',)
print(type(thing))

list[:0] = ['Newham', 'Hackney']
print(list)

list += ['Southwark', 'Barking']
print(list)

list.extend(['Dagenham', 'Croydon'])
print(list)

list.insert(5, 'Tottenham')
print(list)

list[5:5] = ['Edmonton']
print(list)

list2 = list.pop(1)
print(list2)

list3 = list.pop(3)
print('the two items we removed:', list2, 'and', list3, "Now the list is shorter:", list)

list.remove('Edmonton')
print(list)

print(list.count('Brie'))
print(list.index('Brie'))

list.reverse()
print(list)

set1 = {5, 6, 7, 8, 9}
set2 = {10, 11, 12, 13}
print(set1)
print(set2)

set1.remove(9)
print(set1)
set2.add(9)
print(set2)
print(len(set2))

list4 = [1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
list4b = ["cat", "dog", "cat", "dog"]
list4_set = set(list4)
list4 = list(list4_set)
print(list4)



