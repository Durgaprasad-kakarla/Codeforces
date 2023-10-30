t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if a+a>b:
        if x>y:
            print(((x-y)*a)+(y*b))
        else:
            print(((y-x)*a)+(x*b))
    else:
        print((x+y)*a)
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
