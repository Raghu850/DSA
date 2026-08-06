class Solution:
    def lowerBound(self, arr, target):
        # code here
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=target:
                h=mid-1
            else:
                l=mid+1
        return l