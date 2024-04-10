def add_binary_integers(A, B, n):
    aux = 0
    C = [0]*(n+1)
    
    for i in range(n-1,-1,-1):
        print(i," - ",A[i],"+", B[i], "(" ,aux,")")
        
        sum = A[i] + B[i] + aux
        aux = sum // 2
        C[i+1] = sum % 2
    
    C[0] = aux
    
    return C
    
print(add_binary_integers([1,0,1,1],[1,0,1,1],4))