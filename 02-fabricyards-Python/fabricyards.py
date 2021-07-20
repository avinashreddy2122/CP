# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!


def fabricyards(inches):
	# Your code goes here...
	yards = inches/36
	a=int(yards)
	if yards>a:
		a=a+1
		return a
	return a

def fabricexcess(inches):
	# Your code goes here...
	if inches==0:
		return 0

	elif inches<=36:
		fabricexcess = 36-inches
		return fabricexcess
	if inches>36:
		yards=inches/36
	x=int(yards)
	if yards>x:
		x+=1
	a=x*36
	b=a-inches

	return b