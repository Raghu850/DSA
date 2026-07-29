class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        f=float('inf')
        s=float('inf')
        for i in arr:
            if i<f:
                s=f
                f=i
            elif f<i<s:
                s=i
        return [f,s] if s!=float('inf') else [-1]
        