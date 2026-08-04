class Solution:
    def subarrayXor(self, arr, m):
        # code here
        xr=0
        a={0:1}
        cnt=0
        for i in range(len(arr)):
            xr=xr^arr[i]
            x=xr^m
            cnt+=a.get(x,0)
            a[xr]=a.get(xr,0)+1
        return cnt