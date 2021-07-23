# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isPrime(n):
	if n<2:
		return False
	for factor in range(2,n):
		if n%factor ==0:
			return False
	return True
def isPalindrome(n):
	rev =0
	while (n>0):
		dig = n%10
		rev = rev*10+dig
		n = n//10
	return rev

def fun_nth_palindromic_prime(n):
	num=2
	count=0
	while(count<=n):

		if (isPrime(num) and isPalindrome(num)==num):
			count+=1
		num+=1
	return num-1
print(fun_nth_palindromic_prime(15))