arr = [43,224,566,645,678,2,7,-33,-234,5,9,0]


for i in range(1, len(arr)):
    curr = arr[i]
    j =  i-1
    while j >=0 and curr < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = curr
print(arr)

