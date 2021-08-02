# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def tidyNum(n):
    prev = 10
    while(n>0):
        num=n%10
        n=n//10
        if num>prev:
            return False
        prev=num
    return True
def fun_nth_tidynumber(n):
    num=0
    cnt=0
    while(cnt<=n):
        num+=1
        if (tidyNum(num)):
            cnt=cnt+1
        
    return num