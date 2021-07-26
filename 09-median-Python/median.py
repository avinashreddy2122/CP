# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	n = len(a)
	if n==0:
		return None
	a.sort()
	if n%2 == 0:
		median1 = a[n//2]
		# print(median1)
		median2 = a[n//2 -1]
		# print(median2)
		median = (median1+median2)/2
	else:
		median = a[n//2]
	return (median)
print(median([1.1, 2.1, 3.1, 4.1, 5.1]))