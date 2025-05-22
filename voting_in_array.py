def voting(arr):
    
    count = 0  
    candidate = None  

    for num in arr:  
        if count == 0:  
            candidate = num
        if num == candidate:  
            count += 1
        else:  
            count -= 1

    
    count = 0  
    for num in arr:  
        if num == candidate:  
            count += 1

    if count > len(arr) / 2:  
        return candidate  
    else:  
        return "No Majority Element"  


arr = [2, 1, 2, 1, 1, 2, 2]
print(voting(arr))  