# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.
import math
def fun_nearestbusstop(street):
	# a=round(street/8)
	# print(a)
	# if street <=4:
	# 	return 0
	# if street%8==0:
	# 	return street
	# b=str(street/8).split(".")
	# print(b)
	# c=b[1][::-1]
	# d=int(c)%10
	# print(d)
	# if d >5 :
	# 	return a*8
	# else:
	# 	return (a-1)*8

	if street <=4:
		return 0
	if street%8==0:
		return street
	a=street/8
	b=math.floor(a)
	c=a-b
	x=0
	if c<=0.5:
		x=math.floor(a)
		print(x)
	else:
		x=math.ceil(a)
		print(x)
	return x*8
	
print(fun_nearestbusstop(12))


# 	print(a)
# 	b=a*8
# 	print(b)
# 	c=b-street
# 	print(c)
# 	if c < 5:
# 		print((a*8)-street)
# 		print((a-1)*8)
# 		return (a-1)*8
# 	else:
# 		return a*8