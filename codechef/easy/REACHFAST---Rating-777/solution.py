# cook your dish here
import math
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    print(math.ceil(abs(b-a)/k))
    