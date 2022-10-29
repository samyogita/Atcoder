n = int(input())
nums = list(map(int, input().split()))
maximum = max(nums)
pos = 1
for ele in nums:
    if ele == maximum:
        print(pos)
    pos +=1
        

