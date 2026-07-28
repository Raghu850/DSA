# cook your dish here
a=int(input())
for i in range(a):
    b=int(input())
    if b<5:
        print(b)
    else:
        b//=5
        print(b*4)