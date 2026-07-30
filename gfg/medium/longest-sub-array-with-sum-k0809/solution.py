class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        d={}
        sum=0
        m=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==k:
                m=i+1
            if sum-k in d:
                m=max(m,i-d[sum-k])
            if sum not in d:
                d[sum]=i
        return m