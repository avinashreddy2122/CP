# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if (len(m1[0])!=len(m2)):
        return None
    a=[]
    b=0
    x=len(m2[0])
    list1=[]
    k=0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                b=b+(m1[i][k] * m2[k][j])
            a.append(b)   
            b=0
    #return a 
    k=0
    for i in range(len(m1)):
        list2=[]
        for j in range(x):
            list2.append(a[k])
            k=k+1
            if k>=x*len(m1):
                break

        list1.append(list2)
        if k>=x*len(m1):
            break
    return list1
fun_matrixmultiply([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]])






