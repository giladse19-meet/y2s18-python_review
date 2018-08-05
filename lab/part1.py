# Part 1 of the Python Review lab.

def hello_world():
	print("Hello world!")

def greet_by_name(name):
	print("Hello", name)

def encode(x):
	a = int(x + 3953531)
	print("got it")
	return(a)

c = encode(5)

def decode(c):
	b = c - 3953531
	print("good")
	return(b)
print(decode(c))
	