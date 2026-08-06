class Solution:
    def findFloor(self, arr, x):
        # code here
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]<=x:
                l=mid+1
            else:
                h=mid-1
        return h