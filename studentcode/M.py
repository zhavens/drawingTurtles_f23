import turtle
import settings as s


def draw():
     starting_pos = s.yertle.pos()
    
     s.yertle.right(90)
     s.yertle.forward(s.BOX_HEIGHT)
     
     s.yertle.penup()
     s.yertle.left(180)
     s.yertle.forward(s.BOX_HEIGHT)
     
     s.yertle.pendown()
     s.yertle.right(150)
     s.yertle.forward(s.BOX_HEIGHT/2)
     
     s.yertle.left(120)
     s.yertle.forward(s.BOX_HEIGHT/2)
     
     s.yertle.right(150)
     s.yertle.forward(s.BOX_HEIGHT)
        

	# return turtle to top left of
     s.yertle.penup()
     s.yertle.setpos(starting_pos)
     s.yertle.setheading(0)
     s.yertle.pendown()
