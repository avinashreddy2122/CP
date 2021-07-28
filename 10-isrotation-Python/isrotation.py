# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x=str(x)
	y=str(y)
	
	if len(x)!=len(y) or len(x)==0 or len(y)==0:
		return False
	# a=sorted(x,reversed =True)
	# print(a)
	# if a==y :
	# 	return True

	s=0
	while(x[0]!= y[s]):
		s+=1
	# 	# print(s)
	# # print(y)
	y=y[s:]+y[:s]
	# # print(y[s:])
	# # print(y[:s])
	# # print(y)
	s=0
	for i in x:
		if i!=y[s]:
			return False
		s+=1
	return True 
	
print(isrotation(12345,54321))