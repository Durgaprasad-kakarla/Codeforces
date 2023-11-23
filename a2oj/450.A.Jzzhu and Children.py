n,m=map(int,input().split())
lst=list(map(int,input().split()))
nums=[]
for i in range(n):
    nums.append([lst[i],i+1])
while len(nums)>1:
    if nums[0][0]>m:
        nums.append([nums[0][0]-m,nums[0][1]])
        nums.pop(0)
    else:
        nums.pop(0)
print(nums[0][1])
