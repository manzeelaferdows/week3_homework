read_pelican = open("pelican.txt", "r")

for line in open("pelican.txt").readlines():
    print(line, end="")


pelican_content = read_pelican.read()
print("The text above has been 'slurped'. \nThis is an inefficient way of reading a files contents.")
print('The text above is', type(pelican_content))

pelican_list = pelican_content.splitlines()
print(pelican_list)
print('This list contains', len(pelican_list), 'elements')

for line in open("pelican.txt"):
    print(line, end="")
read_pelican.close()
