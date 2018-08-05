# Part 2 of the Python Review lab.

def encode(x, y):
	if 1 < y and y > 250 and 500 < x and x > 1000:
		product = x * y
		print(product)
	else:
		print("Invalid input: Outside range.")
		return


def decode(coded_message):
	pass