class Solution:
    def largest(self, arr):
        # code here
        m=arr[0]
        for i in arr:
            if i>m:
                m=i
        return m