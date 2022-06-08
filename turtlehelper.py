from turtle import *
import turtle
import settings as s

class Count(object):
	char_count = 0  # This is a class attribute
	origin_x = -s.SCREEN_SIZE//2 + s.TURTLE_SPACE
	origin_y = s.SCREEN_SIZE//2 - s.TURTLE_SPACE

def start():
	# initial starting pos is 0,0
	s.yertle.penup()
	s.yertle.setpos((Count.origin_x, Count.origin_y))
	s.yertle.pendown()
	s.yertle.showturtle()


def stop():
	turtle.done()

def drawSquare():
	s.yertle.pencolor("red")
	pos = s.yertle.position()
	for i in range(2):
		s.yertle.forward(s.BOX_WIDTH)
		s.yertle.right(90)
		s.yertle.forward(s.BOX_HEIGHT)
		s.yertle.right(90)
	s.yertle.pencolor("black")

def drawOffset():
	s.yertle.penup()
	s.yertle.setx(s.yertle.position()[0] + s.TURTLE_SIZE + s.TURTLE_SPACE)
	s.yertle.pendown()
	Count.char_count += 1

def newLine():
	positions = s.yertle.pos()
	s.yertle.penup()
	s.yertle.setpos((Count.origin_x - s.TURTLE_SPACE - s.TURTLE_SIZE, \
	Count.origin_y - ((s.BOX_HEIGHT + s.TURTLE_SPACE) * \
	(Count.char_count // s.LETTERS_PER_LINE))))
	s.yertle.pendown()

def checkNewLine(index, sentence):	
	if index < len(sentence) - 1:
		if sentence[index+1] == ' ':
			curr_x = s.yertle.xcor()
			# check how many more letters we can fit on this line
				#where is my turtle x
				# subtract from 500
				# divide by size of letters
				#thats how many more letters i can fit
			space_left = int(s.SCREEN_SIZE/2 - curr_x) // s.LETTERS_PER_LINE
			word_length = 0;
			for i in range(index+2, len(sentence)):
				if sentence[i] == ' ':
					break
				word_length += 1
			if space_left < word_length:
				newLine()


