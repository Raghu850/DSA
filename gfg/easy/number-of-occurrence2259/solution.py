class Solution:
    def countFreq(self, arr, target):
        # code here
        f,l=-1,-1
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                f=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if f==-1:return 0
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                l=mid
                low=mid+1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return l-f+1