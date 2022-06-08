import turtle

def drawE():
	# wn = turtle.Screen()
	# wn.bgcolor("light green")
	# wn.title("Turtle")
	skk = turtle.Turtle()

	# top line
	skk.forward(100)
	skk.backward(100);

	# middle line
	skk.right(90)
	skk.forward(50)
	skk.left(90)
	skk.forward(100)
	skk.backward(100);

	# bottom
	skk.right(90)
	skk.forward(50)
	skk.left(90)
	skk.forward(100)

	turtle.done()