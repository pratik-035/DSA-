
arr = [7, 8, 3, 1, 2] 
n = len(arr) 


# insertio sort logic 
for i in range(1, n): # start from second element 
    key = arr[i] # current element to be inserted 
    j = i - 1
    
    # move elements that are greater than key to one position ahead 
    
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
        
    arr[j+1] = key # insert key at correct position 
    

print("Sorted Array : ", arr)