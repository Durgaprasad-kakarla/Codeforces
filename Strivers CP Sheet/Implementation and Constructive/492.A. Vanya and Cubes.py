n=int(input())
i=1
sm=0
cnt=0
while sm<=n:
    sm+=(i*(i+1))//2
    cnt+=1
    i+=1
print(cnt-1)
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
