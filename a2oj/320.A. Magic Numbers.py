s=int(input())
st=str(s)
st=st.replace('144','-')
st=st.replace('14','-')
st=st.replace('1','-')
st=st.replace('-','')
if st=='':
    print("YES")
else:
    print("NO")
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
