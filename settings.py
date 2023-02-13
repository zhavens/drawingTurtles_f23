from turtle import Turtle, Screen
import turtle

# Settings file with all important information for making
# properly sized letters

def init():
	global screen 
	screen = Screen()
	
	# 800x800 screen size
	screen.setup(800, 800)

	global yertle
	yertle = Turtle(shape="turtle", visible=False)
	
        # the turtle is 20 pixels
	global TURTLE_SIZE
	TURTLE_SIZE = 20

        # the spacing between letters is 10 pixels
	global TURTLE_SPACE
	TURTLE_SPACE = 10

        # each letter can be max 25 pixels wide
	global BOX_WIDTH
	BOX_WIDTH = 25

        # each letter cna be max 50 pixels high
	global BOX_HEIGHT
	BOX_HEIGHT = 50

	global SCREEN_SIZE
	SCREEN_SIZE = 800

        # based on SCREEN_SIZE, this is the number of letters we can put on
        # a line before we need a new line
	global LETTERS_PER_LINE
	LETTERS_PER_LINE = int(SCREEN_SIZE/(TURTLE_SPACE + BOX_WIDTH))
init()
