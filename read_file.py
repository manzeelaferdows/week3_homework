read_pelican = open("pelican.txt", "r")

for line in open("pelican.txt").readlines():
    print(line, end="")

pelican_content = read_pelican.read()
print(type(pelican_content))
pelican_list = pelican_content.splitlines()
print(pelican_list)
print(len(pelican_list))

for line in open("pelican.txt"):
    print(line, end="")
