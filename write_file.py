append = open("pelican.txt", "w")

first_line = append.write("A wonderful bird in the pelican,\n")
print(first_line)

second_line = append.write("His bill holds more than his belican.\n")
print(second_line)

additional_lines = append.writelines(["He can take in his beak,\n", "Enough food for a week,\n", "But I'm surprised if I see how on earth he can.\n"])
print(additional_lines)
#Ask Victoria what to do if the code line is too long

