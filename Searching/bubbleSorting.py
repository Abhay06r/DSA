 
arr = [43,224,566,645,678,2,7,-33,-234,5,9,0]

# make a counter for arr
for i in range(len(arr)-1):
    
    # traverse in arr
    for j in range(len(arr)-i-1):
        
        # comparing 1st and next element 
        if arr[j] > arr[j+1]:
            
            # swap
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
