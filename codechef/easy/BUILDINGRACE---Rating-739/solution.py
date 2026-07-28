# cook your dish here
n=int(input())
for i in range(n):
    a,b,x,y=map(int,input().split())
    chef=a*y
    chefina=b*x
    if chef<chefina:
        print("Chef")
    elif chef>chefina:
        print("Chefina")
    else:
        print("Both")