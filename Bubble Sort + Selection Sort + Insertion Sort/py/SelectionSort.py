
arr = [7, 8, 3, 1, 2]
n = len(arr) 

# selection sort
for i in range(n):
    smallest = i;  # assume current index has the minimum
    
    # Find the index of the smallest element in the remaining array
    for j in range(i+1, n):
        if(arr[j] < arr[smallest]):
            smallest = j
            
    # swap the found minimum with the element at index i
    arr[i], arr[smallest] = arr[smallest], arr[i]
    
print("Sorted Array : ", arr)