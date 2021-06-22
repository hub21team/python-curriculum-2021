###------------------------------------------------- EASY -------------------------------------------------###

# Challenge 1
def read_contents(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except:
        print("An error occured.")
        print("Please check that you have the correct filename.")

filename = input("Enter file to be read: ")
read_contents(filename)

# Challenge 2


###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge 1
def find_squares(lst):
    for elt in lst:
        try:
            sqr = elt ** 2
            print("Square of", elt, "is", sqr)
        except Exception as e:
            print("Sorry,", e.__class__, "occured :(")
        
lst1 = [1, 2, 3]
lst2 = [1, "arda", 'x', 14, 12.34]

find_squares(lst1)
find_squares(lst2)

###------------------------------------------------- HARD -------------------------------------------------###

# Challenge 1







