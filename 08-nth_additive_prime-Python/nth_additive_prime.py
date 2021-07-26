# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def getSum(x):
	sum=0
	while(x!=0):
		sum=sum+x%10
		x=x//10
	return sum

def isPrime(x):
	if x<2 :
		return False
	for factor in range(2,x):
		if x%factor == 0:
			return False
	return True

def fun_nth_additive_prime(n):
	num =2
	count = -1
	while(count<n):
		sum = getSum(num)
		if (isPrime(num) and isPrime(sum)):
			count+=1
		num+=1
	
	return num-1
