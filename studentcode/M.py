# your file must include these 2 imports
import turtle
import settings as s


# you must have a def draw() function
def draw():
    # use s.yertle as your turtle everywhere, no need to make a new turtle
    # this line gets me the turtles current position
    ### (PRE CONDITION: top left of a bounding box) ###
    starting_pos = s.yertle.pos()

    # using s. [box sizes], I draw my letter WITHIN the bounding box
    s.yertle.right(90)
    s.yertle.forward(s.BOX_HEIGHT)
    s.yertle.right(180)
    s.yertle.forward(s.BOX_HEIGHT)
    s.yertle.right(135)
    s.yertle.forward(s.BOX_WIDTH)
    s.yertle.left(90)
    s.yertle.forward(s.BOX_WIDTH)
    s.yertle.right(135)
    s.yertle.forward(s.BOX_HEIGHT)


    ### (POST CONDITION: Return turtle to the expected position) ###
    # Turtle facing correct direction in top left stop
    # so that next letter knows where
    # the correct position in.
    s.yertle.penup()
    s.yertle.setpos(starting_pos)
    s.yertle.setheading(0)
    s.yertle.pendown()

    # Feel free to use any part of this code as a template for your letter
    # know that you can access the box width and height with s.BOX_WIDTH and s.BOX_HEIGHT
    # and you can access the turtle you need to draw with s.yertle.ANYFUNCTIONHERE()
    # you will need the two imports from the top and you need to put ALL your code in a
    # def draw() function

