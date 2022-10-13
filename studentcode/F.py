import turtle
import settings as s

def draw():
    starting_pos = s.yertle.pos()

    s.yertle.forward(s.BOX_WIDTH) #draws line upper full
    s.yertle.right(180)               #changes heading towards left
    s.yertle.forward(s.BOX_WIDTH)       #goes to starting pos facing opposite
    s.yertle.left(90)                       #faces down
    s.yertle.forward(s.BOX_HEIGHT/2)        #goes down half of height
    s.yertle.left(90)                       #turns towards heading 0
    s.yertle.forward(s.BOX_HEIGHT/2)        #draws line half lower 
    s.yertle.right(180)                     #turns heading opposite again
    s.yertle.forward(s.BOX_HEIGHT/2)        #goes back half 
    s.yertle.left(90)                       #faces down
    s.yertle.forward(s.BOX_HEIGHT/2)        #draws lower half of spine

    # return turtle to top left of
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()
