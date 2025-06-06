def maxChunksToSorted(arr):
    
    n = len(arr)
    sorted_arr = sorted(arr)
    
    chunks = 0
    sum_arr = 0
    sum_sorted_arr = 0
    
    for i in range(n):
        sum_arr += arr[i]
        sum_sorted_arr += sorted_arr[i]
        
       
        if sum_arr == sum_sorted_arr:
            chunks += 1
            
    return chunks

arr = [2, 1, 3, 4, 4]
result = maxChunksToSorted(arr)
print(result)

arr = [5, 4, 3, 2, 1]
result = maxChunksToSorted(arr)
print(result)