# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=0
    for i in arr:
        i+=k
        if i%7==0:
            ans+=1
    print(ans)