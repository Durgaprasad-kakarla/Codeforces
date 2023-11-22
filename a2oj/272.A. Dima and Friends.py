n=int(input())
nums=list(map(int,input().split()))
cnt=0
sm=sum(nums)
n=n+1
for i in range(1,6):
    if (sm+i)%n!=1:
        cnt+=1
print(cnt)
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
