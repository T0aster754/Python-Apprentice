import turtle


def set_turtle_image(turtle, pikachu):
   # """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / pikachu)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()
t.speed(5)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, 200)
    t.goto(-200, -200)
    t.goto(200, -200)


turtle.exitonclick() 

#Then change the code so that the turtle has a different image ( look in the 'images'
#directory ) and moves to the corners of the screen in a square pattern. 
#"""

