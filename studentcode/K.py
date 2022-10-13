import turtle
import settings as s


def draw():
    starting_pos = s.yertle.pos()

    s.yertle.right(90)

    s.yertle.forward(s.BOX_HEIGHT)

    s.yertle.penup()

    s.yertle.right(180)

    s.yertle.forward(s.BOX_HEIGHT * 0.75)

    s.yertle.pendown()

    s.yertle.right(45)

    s.yertle.forward(s.BOX_WIDTH)

    s.yertle.penup()

    s.yertle.forward(-s.BOX_WIDTH)

    s.yertle.pendown()

    s.yertle.right(135)

    s.yertle.forward(s.BOX_HEIGHT * 0.25)

    s.yertle.left(45)

    s.yertle.forward(s.BOX_WIDTH + 10)

    # return turtle to top left of
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()
    


