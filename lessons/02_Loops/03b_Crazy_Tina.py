"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [25, 30, 45, 75, 90, 120, 145, 80, 10]
lefts = [30, 45, 90, 75, 20, 15, 20, 10, 50]
colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'orange', 'cyan', 'maroon']

for  i in range(8):

    forward = forwards[6]
    left = lefts[8]
    color = colors[7]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

