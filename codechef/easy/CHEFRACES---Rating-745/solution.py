# cook your dish here
t = int(input())
for _ in range(t):
    X, Y, A, B = map(int, input().split())
    chef = {X, Y}
    rival = {A, B}
    print(2 - len(chef & rival))