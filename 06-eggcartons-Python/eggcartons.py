# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	
	carton = eggs/12
	print(carton)
	if eggs==0:
		return 0
	a= int(carton)
	print(a)
	if (carton > a):
		a+=1
		print(a)
		return a
	return a 
# fun_eggcartons(22)
	
