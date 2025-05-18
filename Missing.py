arr = [1, 2, 4, 5]

count = arr[0]

for i in range(len(arr)):
  if arr[i] == count:
    count = count + 1
  else:
    break;

print(count)
