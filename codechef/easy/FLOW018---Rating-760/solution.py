# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    i=1
    for j in range(2,a+1):
        i*=j
    print(i)