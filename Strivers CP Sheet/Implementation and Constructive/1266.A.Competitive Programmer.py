t=int(input())
for i in range(t):
    st=input()
    cnt_0,cnt_even,sm=0,0,0
    for i in st:
        if i=='0':
            cnt_0+=1
        if int(i)%2==0:
            cnt_even+=1
        sm+=int(i)
    if sm%3==0 and cnt_0==1:
        if cnt_even>1:
            print("red")
        else:
            print("cyan")
    elif sm%3==0 and cnt_0>1:
        print("red")
    else:
        print("cyan")
''' Time Complexity--O(t*n)
    Space Complexity--O(1)'''
