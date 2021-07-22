# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	i=0
	j=0
	x=""
	if len(s1)>len(s2):
		j=len(s2)
	else:
		j=len(s1)
	while(i<j):
		x=x+s1[i]+s2[i]
		i+=1
	if j==len(s1):
		x=x+s2[j:]
	else:
		x=x+s1[j:]
	return x

	