n,k=map(int,input().split())
if n&1==1:
    if k<=(n//2+1):
        print(2*k-1)
    else:
        x=k-(n//2+1)
        print(2*x)
else:
    if k<=n//2:
        print(2*k-1)
    else:
        x=k-n//2
        print(2*x)
'''Time Complexity--O(1)
   Space Complexity--O(1)'''
