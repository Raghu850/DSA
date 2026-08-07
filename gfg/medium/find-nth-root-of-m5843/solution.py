class Solution:
    def nthRoot(self, n, m):
       # code here
       l,h=0,m
       while l<=h:
           mid=(l+h)//2
           cur=mid**n
           if cur==m:
               return mid
           elif cur<m:
               l=mid+1
           else:
               h=mid-1
       return -1