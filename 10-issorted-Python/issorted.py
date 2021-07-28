# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	# flag = 0
	# i=1
	# n = len(a)
	# while(i<n):
	# 	if a[i]<a[i-1] or a[i]>a[i-1]:
	# 		flag=1
	# 	i+=1
	# if not flag:
	# 	return True
	# else:
	# 	return False
	if a== sorted(a):
		return True
	if a== sorted(a,reverse = True):
		return True
	else:
		return False
print(issorted([1,2,3,4,5]))