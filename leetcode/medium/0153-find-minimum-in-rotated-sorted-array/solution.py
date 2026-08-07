class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        m=float('inf')
        while l<=r:
            mid=(l+r)//2
            if nums[l]<=nums[mid]:
                m=min(nums[l],m)
                l=mid+1
            else:
                m=min(nums[mid],m)
                r=mid-1
        return m
                
            