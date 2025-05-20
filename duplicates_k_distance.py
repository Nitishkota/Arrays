def check_duplicates_within_k(arr, distance):
    
    for i in range(len(arr)):
        for j in range(i + 1, min(i + distance + 1, len(arr))): 
            if arr[i] == arr[j]:
                return True  
    return False  


arr = [1, 2, 3, 1]
distance = 3
result = check_duplicates_within_k(arr, distance)
print(result)  