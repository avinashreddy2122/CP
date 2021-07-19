# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a=int(pow((x1-x2),2))+int(pow((y1-y2),2))
	b=int(pow((x2-x3),2))+int(pow((y2-y3),2))
	c=int(pow((x3-x1),2))+int(pow((y3-y1),2))

	if ((a>0 and b>0 and c>0) and (a==(b+c) or b==(a+c) or c==(a+b))):
		return True
	else:
		return False


