"""
Write a program that simulates what we should do at a traffic light. We will write a program that takes the light color as an input `red`, `yellow`, or `green`, and depending on the light color we will print the required actions: `move`, `stop`, `prepare to move`. Use If-Elif Statements.
"""

light_color = input("Please enter light color")

if light_color == "red":
    print("stop")
elif light_color == "yellow":
    print("prepare to move")
elif light_color == "green":
    print("move")
