class Solution:
    def leaders(self, arr):
        # code here
        res=[]
        n=len(arr)
        m=arr[-1]
        res.append(m)
        for i in range(n-2,-1,-1):
            if arr[i]>=m:
                m=arr[i]
                res.append(m)
        res.reverse()
        return res