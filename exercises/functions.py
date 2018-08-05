# Write your solution for 1.4 here!

def is_prime(a):
	for i in range(a-1, 2 ,-1):
		if a % i == 0:
			print("not prime")
			return(False)
	return("prime")
	print("prime")
	print(a)

print(is_prime(11))
