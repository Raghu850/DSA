class Solution:
    def findCeil(self, arr, x):
        # code here
        if x>arr[-1]:
            return -1
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=x:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
