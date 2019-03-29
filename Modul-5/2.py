A = [23,3673,673647,156246]
B = [2367,863468,8648]

C = A+B
for i in range(len(C)): 
    min_idx = i 
    for j in range(i+1, len(C)): 
        if C[min_idx] > C[j]: 
            min_idx = j 
    
    C[i], C[min_idx] = C[min_idx], C[i]

print (C)
