# cook your dish here
import math
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    c//=30
    a+=c
    print(math.ceil(a/b))