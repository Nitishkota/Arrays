def inter_arr(arr1, arr2):
  inter = []
  for i in arr1:
    if i in arr2:
      inter.append(i)
  return inter

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(inter_arr(arr1, arr2))