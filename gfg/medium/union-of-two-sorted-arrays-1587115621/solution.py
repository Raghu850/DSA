class Solution:
    def findUnion(self, a, b):
        # code here 
        i,j=0,0
        ans=[]
        n=len(a)
        m=len(b)
        while i<n and j<m:
            if a[i]<=b[j]:
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
            else:
                if not ans or ans[-1]!=b[j]:
                    ans.append(b[j])
                j+=1
        while i<n:
            if ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1
        while j<m:
            if ans[-1]!=b[j]:
                ans.append(b[j])
            j+=1
        return ans
        