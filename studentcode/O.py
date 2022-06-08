import turtle
import settings as s

def draw():
	starting_pos = s.yertle.pos()
	s.yertle.penup()
	s.yertle.setpos((starting_pos[0] + s.BOX_WIDTH//2 + 6, \
	starting_pos[1] - (s.BOX_HEIGHT)))
	s.yertle.pendown()

	s.yertle.left(45)
	for i in range(2):      # Draws 2 halves of ellipse
		s.yertle.circle(s.BOX_HEIGHT*.65,90)    # Long curved part
		s.yertle.circle(s.BOX_WIDTH*.3,90)  # Short curved part

	# return turtle to top left of
	s.yertle.penup()
	s.yertle.setpos(starting_pos)
	s.yertle.setheading(0)
	s.yertle.pendown()