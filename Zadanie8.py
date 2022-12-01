import string
import random

list = []

# Creating list [a-z,0-9]
for i in string.ascii_lowercase:
    list.append(i)
for i in range(9):
    list.append(i)
print(list)

lines = random.randrange(50,301)
print(lines)

text_file = open("file.txt", "w")
for i in range(lines):
    chars = random.randrange(3,21)
    print(chars)
    for x in range(chars):
        char = list[random.randrange(0, len(list))]
        text_file.write(format(str(char)))
    text_file.write('\n')


print("Lines: {}".format(lines))

text_file.close()

text_file = open("file.txt")
print(text_file.readlines())
