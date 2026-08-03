class Solution:
    def maxLength(self, arr):
        # code here
        a={}
        maxi=0
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==0:
                maxi=i+1
            else:
                if sum in a:
                    maxi=max(maxi,i-a[sum])
                else:
                    a[sum]=i
        return maxi