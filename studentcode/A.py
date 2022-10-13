#To provide instructions to the turtle on how to draw the letter "A"

import turtle                               #imports turtle
import settings as s                        #import settings as the variable 's'

#begins the instructions to draw the assigned letter

def draw():
    starting_pos = s.yertle.pos()
    s.yertle.penup()                        #moves turtle to bottom left of box
    s.yertle.right(90)
    s.yertle.forward(s.BOX_HEIGHT)
    s.yertle.pendown()

    s.yertle.left(165)                      #makes the first(left) side of the letter
    s.yertle.forward(s.BOX_HEIGHT)
    
    s.yertle.right(150)                     #makess the second(right) side of the letter
    s.yertle.forward(s.BOX_HEIGHT)
    
    s.yertle.left(180)                      #moves the turtle to the middle of the letter
    s.yertle.penup()
    s.yertle.forward(s.BOX_HEIGHT/2)
    s.yertle.pendown()
    
    s.yertle.left(75)                       #finishes the letter 'A' by making the middle line between the two sides
    s.yertle.forward(s.BOX_WIDTH/2)

    # return turtle to top left of
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()
