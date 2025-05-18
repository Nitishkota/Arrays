def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:  
      return False  
  return True  

arr = [1, 2, 2, 4, 5]
result = is_sorted(arr)
print(result)  

arr2 = [1, 3, 2, 4, 5]
result2 = is_sorted(arr2)
print(result2)  