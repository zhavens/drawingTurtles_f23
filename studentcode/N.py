import turtle
import settings as s

def draw():
	starting_pos = s.yertle.pos()

	s.yertle.right(90)
	s.yertle.forward(s.BOX_HEIGHT)
	s.yertle.left(180)
	s.yertle.forward(s.BOX_HEIGHT)

	s.yertle.right(155)
	s.yertle.forward(55)
	s.yertle.left(155)
	s.yertle.forward(s.BOX_HEIGHT)

	# return turtle to top left of
	s.yertle.penup()
	s.yertle.setpos(starting_pos)
	s.yertle.setheading(0)
	s.yertle.pendown()
