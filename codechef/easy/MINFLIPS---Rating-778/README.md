# MINFLIPS - Rating 778

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T14:29:11.244Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/MINFLIPS)