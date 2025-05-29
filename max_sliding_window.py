from collections import deque

def max_sliding_window(nums, k):
    
    if not nums:
        return []

    n = len(nums)
    if k > n:
        return []

    output = []
    
    dq = deque()

    for i in range(n):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            output.append(nums[dq[0]])

    return output

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_sliding_window(nums, k)
print(result)