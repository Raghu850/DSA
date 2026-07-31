# cook your dish here
import math
t=int(input())
for _ in range(t):
    h,x,y=map(int,input().split())
    ans=1
    ans+=math.ceil((h-y)/x)
    print(ans)