n=int(input())
nums=list(map(int,input().split()))
q=int(input())
queries=list(map(int,input().split()))
dic={}
for i in range(n):
    dic[nums[i]]=i
sasha_cnt,petya_cnt=0,0
for i in queries:
    sasha_cnt+=dic[i]+1
    petya_cnt+=(n-dic[i])
print(sasha_cnt,petya_cnt)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
