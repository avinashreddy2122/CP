def isMagicSquare(n):
    a=len(n)

    diagonalsum1=0
    diagonalsum2=0
    for i in range(a): # i,i as diagonals top left to botmrigh
        diagonalsum1+=n[i][i]
        diagonalsum2+=n[i][a-i-1]
    print(diagonalsum1,diagonalsum2)
    if not(diagonalsum1==diagonalsum2):
        return False
    
    for i in range(a):
        rowsum = 0
        colsum = 0
        for j in range(a):
            rowsum+=n[i][j]
            colsum+=n[j][i]
    print(rowsum,colsum)
    if not (rowsum==colsum==diagonalsum1):
        return False
    return True
   

# isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
isMagicSquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]])