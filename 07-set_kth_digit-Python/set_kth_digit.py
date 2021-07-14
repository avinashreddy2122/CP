# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):

	flag=False
	if n<0:
		n=-n
		flag=True
	cnt=0
	res=0
	while(n>0):
		r=n%10
		if cnt==k:
			res += (d*(10**cnt))
		else:
			res=res+(r*(10**cnt))
		cnt+=1
		n=n//10

	while cnt<=k:
		if cnt==k:
			res=res+(d*(10**cnt))
		
		cnt+=1
	if flag:
		return (-res)
	else:
		return res
	
