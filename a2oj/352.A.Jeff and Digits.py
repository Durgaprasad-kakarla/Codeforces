n=int(input())
nums=list(map(int,input().split()))
count_5=nums.count(5)
count_0=nums.count(0)
if count_5>8 and count_0>0:
    x=(count_5//9)*9*'5'+('0'*count_0)
    print(int(x))
elif count_0==0:
    print(-1)
else:
    print(0)
''' Time Complexity--O(n)
    Space Complexity--O(1)
