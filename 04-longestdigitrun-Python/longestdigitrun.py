# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	count=1
	value=0
	res=0
	prev=-1
	v=abs(n)
	while(v>0):
		rem=v%10
		if(rem!=prev):
			count=1
		v=v//10
		if(prev==rem):
			count=count+1
		prev=rem
		if (count>value):
			value=count
			res=prev
		if(value==count):
			if(res>prev):
				res=prev
	return res       