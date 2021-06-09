###------------------------------------------------- EASY -------------------------------------------------###

# challenge 1
def file_read(fname):
    txt = open(fname)
    print(txt.read())

daffodils = "Daffodils.txt"
file_read(daffodils)

# challenge 2
my_file = open("hub21.txt", "r+")

line1 = "Coding is the key to the future."
line2 = "There is no skill more important in the 21st century than coding."
line3 = "That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities."
my_file.write(line1)
my_file.write(line2)
my_file.write(line3)

file_data = my_file.read()
print(file_data)
my_file.close()

###------------------------------------------------- MEDIUM -------------------------------------------------###

# challenge 1

file = open("life_lessons.txt", "r+")
text = "And once the storm is over,  " \
       "you won’t remember how you made it through, " \
       "how you managed to survive. You won’t even be sure," \
       " whether the storm is really over. But one thing is certain. " \
       "When you come out of the storm, you won’t be the same person who walked in. " \
       "That’s what this storm’s all about. " \
       "" \
       "― Haruki Murakami, Kafka on the Shore"

file.write(text)








