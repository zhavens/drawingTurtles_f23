import turtle
import settings as s
#version two of the K 

def draw():
    starting_pos = s.yertle.pos()

    s.yertle.right(90)

    s.yertle.forward(s.BOX_HEIGHT)

    s.yertle.penup()

    s.yertle.right(180)

    s.yertle.forward(s.BOX_HEIGHT/2)

    s.yertle.pendown()

    s.yertle.right(45)

    s.yertle.forward(s.BOX_WIDTH*1.4)#DID MATH TO GET THE DIAGONAL LENGTH AND THEN GOT THE RATIO OF IT TO WIDTH

    s.yertle.right(180)#turn it around and repeat basically
    s.yertle.forward(s.BOX_WIDTH*1.4)
    s.yertle.left(90)
    s.yertle.forward(s.BOX_WIDTH*1.4)
    
                   
    
    

    # return turtle to top left of
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()
    


