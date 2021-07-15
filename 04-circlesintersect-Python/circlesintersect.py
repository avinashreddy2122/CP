# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
	c1c2=((x1-x2)**2 + (y1-y2)**2)**0.5
	print(c1c2)
	c=r1+r2
	print(c)
	if int(c1c2) <= int(c):
		print(True)
		return True
	print(False)
	return False
fun_circlesintersect(-10, 8, 30, 14, -24, 10)
