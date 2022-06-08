import sys
import os
import string
import studentcode.E as E

alphabet_string = string.ascii_uppercase
alphabet = list(alphabet_string)

# for letter in alphabet: 
# 	try:
# 		import studentcode.E as E
# 	except ImportError:
#		print('import file, no file E')

def main():
	thismodule = sys.modules[__name__]
	for letter in alphabet:
		try:
			func = getattr(thismodule, letter)
			func.draw()
		except:
			print('no ' + letter)

print("Start Alphabet")
main()
print("End Alphabet")



