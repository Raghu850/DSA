# cook your dish here
t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    mini=11
    total=0
    for i in a:
        if i<mini:
            mini=i
        total+=i
    print(total-mini)