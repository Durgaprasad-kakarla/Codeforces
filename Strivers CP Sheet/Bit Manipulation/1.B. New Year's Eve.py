n,k=map(int,input().split())
binary=list(bin(n)[2:])
x=len(binary)
i=0
if k==1:
    print(n)
else:
    while i<x:
        if binary[i]=='0':
            binary[i]='1'
        i+=1
    st="".join(binary)
    print(int(st,2))
''' Time Complexity--O(32)
    Space Complexity--O(32)'''
