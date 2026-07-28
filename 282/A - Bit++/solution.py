import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    x=0
    for _ in range(t):
        op=input()
        if '++' in op:
            x+=1
        else:
            x-=1
    print(x)
            
if __name__ == "__main__":
    main()