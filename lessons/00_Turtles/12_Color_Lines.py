"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the windowgfbfvsdsgdfg

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
forward = 50
left = 90
colors = [ 'red', 'blue', 'black', 'green']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


for color in colors[::-1]:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)



# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.exitonclick()                     # Close the window when we click on it