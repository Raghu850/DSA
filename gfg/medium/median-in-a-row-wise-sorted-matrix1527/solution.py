class Solution:
    def median(self, mat):
    	# code here 
     rows = len(mat)
     cols = len(mat[0])

     low = min(row[0] for row in mat)
     high = max(row[-1] for row in mat)

     required = (rows * cols + 1) // 2

     while low <= high:
         mid = (low + high) // 2

         count = 0

         # Count elements <= mid
         for row in mat:
             l = 0
             r = cols

             while l < r:
                 m = (l + r) // 2

                 if row[m] <= mid:
                     l = m + 1
                 else:
                     r = m

             count += l

         if count < required:
             low = mid + 1
         else:
             high = mid - 1

     return low