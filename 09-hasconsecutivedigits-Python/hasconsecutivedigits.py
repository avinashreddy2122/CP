# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n=abs(n)
	prev =-1
	while(n>0):
		newdigit = n%10
		if newdigit == prev :
			print(newdigit,prev)
			return True
		prev = newdigit

		n=n//10	
	return False
hasconsecutivedigits(26011)