import sys
import os
import string
import importlib
import turtlehelper as th

# Set up aa list of letters [A,B,C,D...]
alphabet_string = string.ascii_uppercase
alphabet = list(alphabet_string)

# This is the sentence we are writing out
sentence_string = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
sentence = list(sentence_string.strip()) # trim whitespace

# Try to import all the files if they exist
# This loop goes through each letter looking for a file A.py, B.py etc etc
# If it finds it, it will load your file into the project

for letter in alphabet:
	module_path = os.path.join("studentcode", letter + ".py")
	if os.path.exists(module_path):
		# Import and load the module from file
		spec = importlib.util.spec_from_file_location(letter,module_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)

		# Set the module to a variable with its letter name
		setattr(sys.modules[__name__], letter, module)

# main function()
# A list of letters are imported from the loop above and
# the code will run the draw() from the existing letter python files

def main():
	th.start()
	thismodule = sys.modules[__name__]
	index = 0
	for index in range(len(sentence)):
		try:
			if sentence[index] != ' ':
				clas = getattr(thismodule, sentence[index])
				clas.draw()
		except:
			th.drawSquare()
			print(sentence[index] + " not yet implemented")
		th.drawOffset()
		th.checkNewLine(index, sentence)
	th.stop()
main()
