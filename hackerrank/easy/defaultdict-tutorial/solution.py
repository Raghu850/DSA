# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = input().split(" ")
A = []
B = []
result = defaultdict(list)

for i in range(int(n)):
    A.append(input())

for j in range(int(m)):
    B.append(input())
    
for pos, thing in enumerate(A):
    result[thing].append(pos+1)


for item in B:
    if item in result.keys():
        print(*result[item])
    else:
        print('-1')
