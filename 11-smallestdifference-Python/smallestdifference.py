# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	a.sort()
	print(a)
	diff = 0
	b=len(a)

	if len(a)  == 0:
		return -1

	smalldifference = abs(a[0]-a[1])
	print(smalldifference)

	for i in range(b-1):
		diff = abs(a[i]-a[i+1])
		if diff<smalldifference:
			smalldifference = diff
	return smalldifference

smallestdifference([-59,-36,-13,1,-53,-92,-2,-96,-54,75])
