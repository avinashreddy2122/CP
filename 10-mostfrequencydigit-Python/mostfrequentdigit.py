# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def digitcount(n,i):
	count=0
	while(n>0):
		a=n%10
		if a==i:
			count+=1
		n=n//10
	return count

def mostfrequentdigit(n):
	# your code goes here
	value=0
	count= 0
	v=abs(n)
	while(v>0):
		rem = v%10
		c= digitcount (abs(n), rem)
		if c>=count :
			if count == c and value > rem :
				value = rem
			elif c>count :
				count = c
				value = rem
		v = v//10

	return value


