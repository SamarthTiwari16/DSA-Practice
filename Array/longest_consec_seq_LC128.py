nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
n = len(nums)
# Brute force TC=O(N2) SC=O(1)
max_count = 0
for i in range(0, n):
    num = nums[i]
    count = 1
    while num+1 in nums:
        count += 1
        num = num+1
    max_count = max(max_count, count)
print(max_count)

# Better solution TC=O(NlogN+N) SC=O(1)
nums.sort()
count=0
last_smaller=float('-inf')
longest=0
for i in range(0, n):
    num = nums[i]
    if num-1 == last_smaller:
        count += 1
        last_smaller = num
    elif num != last_smaller:
        count = 1
        last_smaller = num
    longest = max(longest, count)
print(longest)

# Optimal solution TC=O(N) SC=O(1)
n = len(nums)
my_set = set(nums)
longest = 0
for i in my_set:
    if i-1 not in my_set:
        x = i
        count=1
        while x+1 in my_set:
            count+=1
            x+=1
        longest = max(longest, count)
print(longest)
