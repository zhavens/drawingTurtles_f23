import inspect

def callAlphabet():
	if ("drawA" in dir()):
		drawA()
	else:
		print("no A yet")

def main():
	print("Start Alphabet")
	callAlphabet()
	print("End Alphabet")

main()


# drinks