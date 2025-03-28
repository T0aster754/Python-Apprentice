
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle  # Tell Python we want to work with the turtle

# Set up the window
turtle.setup(width=600, height=600)

tina = turtle.Turtle()

tina.shape('turtle')

tina.speed(2)

def draw_polygon(sides, side_length):
    angle = 360 / sides  
    for _ in range(sides):
        tina.forward(side_length)
        tina.left(angle)

# Function to draw a square
def draw_square(side_length):
    tina.penup()
    tina.goto(-100, 100)  
    tina.pendown()
    for _ in range(4):
        tina.forward(side_length)
        tina.left(90)

# Function to draw a pentagon
def draw_pentagon(side_length):
    tina.penup()
    tina.goto(30, 90)
    tina.pendown()
    for _ in range(5):
        tina.forward(side_length)
        tina.left(72)  

# Function to draw a hexagon
def draw_hexagon(side_length):
    tina.penup()
    tina.goto(-100, -90) 
    tina.pendown()
    for _ in range(6):
        tina.forward(side_length)
        tina.left(60) 

draw_square(50)   
tina.penup()
tina.goto(200, 0)  
tina.pendown()
draw_pentagon(75)  
tina.penup()
tina.goto(-200, 0) 
tina.pendown()
draw_hexagon(100)  

turtle.exitonclick()       
