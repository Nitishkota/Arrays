arr = [0, 1, 0, 2, 3, 4, 5]

for i in range(len(arr)):
  if (arr[i] == 0):
    arr.append(arr[i])
    arr.remove(arr[i])
print(arr)