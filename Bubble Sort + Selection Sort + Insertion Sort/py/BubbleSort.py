
arr = [7, 8, 3, 1, 2]

n = len(arr)

# outer loop for passes 
for i in range(n-1):
    
    # inner loop for comparing different elements
    for j in range(n - 1 - i):
        if(arr[j] > arr[j+1]):
            
            # swap if elements are in wrong order
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Sorted Array : ", arr)