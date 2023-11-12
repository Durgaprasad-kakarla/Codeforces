s=input()
s=list(s.replace('+',''))
s.sort()
st=""
for i in s:
    st=st+i+'+'
print(st[:-1])
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
