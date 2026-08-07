class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        low =1
        high=stalls[-1]-stalls[0]
        def canPlace(stalls,k,mid):
            count=1
            last=stalls[0]
            for i in range(len(stalls)):
                if stalls[i]-last>=mid:
                    count+=1
                    last=stalls[i]
                    if count==k:
                        return True
            return False
        while low<high:
            mid=(low+high+1)//2
            if canPlace(stalls,k,mid):
                low=mid
            else:
                high=mid-1
        return low