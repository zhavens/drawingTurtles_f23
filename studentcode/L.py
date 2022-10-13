import turtle
import settings as s
"""Draws a L

     Pre-conditions: turtle named s.yertle exists, and pen is down,
        postion already defined
       all the varibles are named
  """


def draw():
	starting_pos = s.yertle.pos()
	
        
	s.yertle.right(90)
	s.yertle.forward(s.BOX_HEIGHT)
	s.yertle.left(90)
	s.yertle.forward(s.BOX_WIDTH/2)


	# return turtle to top left of
	s.yertle.penup()
	s.yertle.setpos(starting_pos)
	s.yertle.setheading(0)
	s.yertle.pendown()




"""Draws a L

     post-conditions:

     turtle should finish write L inside only box on the screen.
     the turtle has return to the top left
  """
