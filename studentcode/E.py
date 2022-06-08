import turtle
import settings as s

def draw():

	starting_pos = s.yertle.pos()

	# top line
	s.yertle.forward(s.BOX_WIDTH)
	s.yertle.backward(s.BOX_WIDTH);

	# middle line
	s.yertle.right(90)
	s.yertle.forward(s.BOX_HEIGHT/2)
	s.yertle.left(90)
	s.yertle.forward(s.BOX_WIDTH)
	s.yertle.backward(s.BOX_WIDTH);

	# bottom
	s.yertle.right(90)
	s.yertle.forward(s.BOX_HEIGHT/2)
	s.yertle.left(90)
	s.yertle.forward(s.BOX_WIDTH)

	# return turtle to top left of
	s.yertle.penup()
	s.yertle.setpos(starting_pos)
	s.yertle.pendown()