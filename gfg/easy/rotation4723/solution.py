class Solution:
    def findKRotation(self, arr):
        # code here
        l,h=0,len(arr)-1
        while l<h:
            mid=(l+h)//2
            if arr[mid]>arr[h]:
                l=mid+1
            else:
                h=mid
        return l