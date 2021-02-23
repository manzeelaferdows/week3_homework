pelican_file = open("pelican.txt", "w")

first_line = pelican_file.write("A wonderful bird in the pelican,\n")
print(first_line)

second_line = pelican_file.write("His bill holds more than his belican.\n")
print(second_line)

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how on earth helican.\n"]

additional_lines = pelican_file.writelines(lines)
print(additional_lines)

pelican_file.close()

# Ask Victoria what to do if the code line is too long
# Answer: make the list into a variable and then use the new variable with the function
