# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def isPrime(n):
	if n<2:
		return False
	for factor in range(2,n):
		if n%factor == 0:
			return False
	return True
def SquareDigits(n):
	sum=0
	while(n>0):
		sum=sum+(n%10)**2
		n=n//10
	return sum
def isHappy(n):
	while(True):
		if n==1:
			return True
		elif n==4:
			return False
		else:
			n=SquareDigits(n)
	return False

def fun_nth_happy_prime(n):
	num = -1
	temp =2
	while(True):
		if (isPrime(temp) and isHappy(temp)):
			num+=1
		if num==n:
			break
		temp+=1

	return temp