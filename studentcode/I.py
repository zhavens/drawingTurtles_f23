import turtle
import settings as s

def draw():
    starting_pos = s.yertle.pos()
#I LIKE A T BUT WITH A BASE, WITH THAT IN MIND I JUST COPIED T CODE THEN DID THE BASELINE 
    s.yertle.forward(s.BOX_WIDTH)
    s.yertle.right(180)
    s.yertle.forward(s.BOX_WIDTH/2)
    s.yertle.left(90)
    s.yertle.forward(s.BOX_HEIGHT)
    s.yertle.left(90)
    s.yertle.forward(s.BOX_WIDTH/2)
    s.yertle.right(180)
    s.yertle.forward(s.BOX_WIDTH)
	

	# return turtle to top left of
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()
    
