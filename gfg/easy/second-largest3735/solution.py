class Solution:
    def getSecondLargest(self, arr):
        # code here
        f=arr[0]
        s=-1
        for i in arr:
            if i>f:
                s=f
                f=i
            elif i<f and i>s:
                s=i
        return s