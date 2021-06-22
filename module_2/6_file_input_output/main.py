###------------------------------------------------- EASY -------------------------------------------------###

# Challenge 1
## 1st solution
def file_read(fname):
    txt = open(fname)
    print(txt.read())

daffodils = "Daffodils.txt"
file_read(daffodils)

## 2nd solution
with open("Daffodils.txt") as f:
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    print(line)


# Challenge 2
## first solution
my_file = open("hub21.txt", "w+")

line1 = "Coding is the key to the future.\n"
line2 = "There is no skill more important in the 21st century than coding.\n"
line3 = "That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities."
my_file.write(line1)
my_file.write(line2)
my_file.write(line3)

file_data = my_file.read()
print(file_data)
my_file.close()

## second solution
with open("hub21.txt", "w") as f:
  line_1 = "Coding is the key to the future.\n"
  line_2 = "There is no skill more important in the 21st century than coding.\n"
  line_3 = "That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities. "
  f.write(line_1)
  f.write(line_2)
  f.write(line_3)
  
with open("hub21.txt") as f:
  info = f.read()
  print(info)

## third solution
with open("hub21.txt", "w+") as f:
    line_1 = "Coding is the key to the future.\n"
    line_2 = "There is no skill more important in the 21st century than coding.\n"
    line_3 = "That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities. "
    f.write(line_1)
    f.write(line_2)
    f.write(line_3)

    info = f.read()
    print(info)

###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge 1

with open("life_lessons.txt", "w") as fl:

    text = "\"And once the storm is over, \
        \nyou won’t remember how you made it \
        \nthrough, how you managed to survive. \
        \nYou won’t even be sure, \
        \nwhether the storm is really over. \
        \nBut one thing is certain. \
        \nWhen you come out of the storm, \
        \nyou won’t be the same person who walked in. \
        \nThat’s what this storm’s all about.\"\n \
        \n― Haruki Murakami, Kafka on the Shore"
    fl.write(text)

with open("life_lessons.txt") as fl:
    data = fl.read()
    num = data.lower().count("you")
    print("The word 'you' is used", num, "times.")



# Challenge 2
with open("books.txt") as f:
    lines = f.readlines()
    lines.sort()

    with open("books_sorted.txt", 'w') as new_f:
        new_f.writelines(lines)


###------------------------------------------------- HARD -------------------------------------------------###

# Challenge 1

def count_occurances(file_name):
    occurances = {}
    with open(file_name) as f:
        data = f.read()
        data = data.lower()

        special_chars = "!,-.\"" # more characters can be added
        for char in special_chars:
            data = data.replace(char, " ")

        words = data.split()
        for word in words:
            if word not in occurances:
                num = data.count(word)
                occurances[word] = num
    return occurances

results = count_occurances("life_lessons.txt")
print(results)


# Challenge 2
with open("books.txt") as f:
    lines = f.readlines()
    first_line = lines[0]
    lines.remove(first_line)
    lines = list(set(lines))
    lines.sort()
    
    new_lines = [first_line]
    new_lines.extend(lines)

    with open("books_sorted_fixed.txt", 'w') as new_f:
        new_f.writelines(new_lines)

