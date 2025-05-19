def print_frequencies(arr):
  seen = []  
  for num in arr:
    if num not in seen:
      count = arr.count(num)  
      print(f"{num}:{count}", end=", ")  
      seen.append(num)  

arr = [1, 2, 2, 3, 1]
print_frequencies(arr)  