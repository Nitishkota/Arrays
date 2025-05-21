def sub_arr_tar(arr, tar):
    count = 0  
    for i in range(len(arr)):  
        current_sum = 0  
        for j in range(i, len(arr)):  
            current_sum += arr[j]  
            if current_sum == tar:  
                count += 1  
    return count  


arr = [1, 1, 1]
tar = 1
print(sub_arr_tar(arr, tar))  