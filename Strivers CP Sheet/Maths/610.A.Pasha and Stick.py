n=int(input())
if n&1==1:
    print(0)
else:
    x=n//2
    if x&1==0:
        print(x//2-1)
    else:
        print(x//2)
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
