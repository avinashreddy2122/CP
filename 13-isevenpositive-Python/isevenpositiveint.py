# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	# b = x.isalpha()
	# print(b)
	# if b == True :
	# 	return False
	if type(x)==int:

		n=abs(x)
		# print(n)
		# if x==None:
		# 	return False
		if  x == n and n%2==0:
			print("True")
			return True
		else: 
			print("false")
			return False
	else: 
		print("false")
		return False
	
	
isevenpositiveint([55])
