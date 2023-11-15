t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a*2>b:
        print(-1,-1)
    else:
        print(a,a*2)
''' Time Complexity--O(t)
    Space Complexity--O(1)'''
