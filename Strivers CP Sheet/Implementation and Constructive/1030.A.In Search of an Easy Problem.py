n=int(input())
flag=0
lst=list(map(int,input().split()))
for i in range(n):
    if lst[i]==1:
        print("HARD")
        flag=1
        break
if flag==0:
    print("EASY")
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
