def sort():
    
    a = [7,5,10,1,9]
    
    for i in range(len(a)):
    
        for j in range(len(a)):
            
            if a[j] > a[i]:
                guardado = a[j]
                a[j] = a[i]
                a[i] = guardado
                
    return a
                
a = sort()

print(a)