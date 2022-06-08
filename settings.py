from turtle import Turtle, Screen
import turtle

def init():
	global screen 
	screen = Screen()
	screen.setup(800, 800)

	global yertle
	yertle = Turtle(shape="turtle", visible=False)
	

	global TURTLE_SIZE
	TURTLE_SIZE = 20

	global TURTLE_SPACE
	TURTLE_SPACE = 10

	global BOX_WIDTH
	BOX_WIDTH = 25

	global BOX_HEIGHT
	BOX_HEIGHT = 50

	global SCREEN_SIZE
	SCREEN_SIZE = 800

	global LETTERS_PER_LINE
	LETTERS_PER_LINE = int(SCREEN_SIZE/(TURTLE_SPACE + BOX_WIDTH))
init()