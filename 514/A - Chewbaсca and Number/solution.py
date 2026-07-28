import sys
 
input = sys.stdin.readline
 
def main():
    t = input().strip()
    # t = int(input())
    ans=""
    for i,ch in enumerate(t):
        d=int(ch)
        if i==0 and d==9:
            ans+='9'
        else:
            ans+=str(min(d,9-d))
    print(ans) 
 
if __name__ == "__main__":
    main()