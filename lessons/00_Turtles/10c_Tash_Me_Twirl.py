
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

import turtle

def set_background_image(window, emoji):
    #"""Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / emoji)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen

def set_turtle_image(turtle, moustache1):
    from pathlib import Path
    image_dir = Path (__file__).parent / "images"
    image_path = str(image_dir / moustache1)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

    # Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "moustache1.gif")

t.penup()

# This is the function that gets called when you click on the screen
def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def moustache1_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """
    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: moustache1_clicked(t, x, y))

turtle.done() 

