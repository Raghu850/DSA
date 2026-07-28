# cook your dish here
a,b,c=map(int,input().split())
b=20-b
b=(b*36)
print("YES" if a<b+c else "NO")