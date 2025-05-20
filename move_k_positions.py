def move_postions(arr, k):
  for i in range(k):
    temp = arr[0]
    for j in range(len(arr)-1):
      arr[j] = arr[j+1]
    arr[len(arr)-1] = temp
  return arr

arr = [1,2,3,4,5]
k = 2
print(move_postions(arr, k))