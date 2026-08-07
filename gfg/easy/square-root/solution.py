class Solution:
    def floorSqrt(self, n): 
        # code here
        l,h=1,n
        ans=1
        while l<=h:
            mid=(l+h)//2
            cur=mid*mid
            if cur<=n:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans