class Solution:
    def searchMatrix(self, mat, x): 
    	# code here 
    	rows = len(mat)
        cols = len(mat[0])
    
        row = 0
        col = cols - 1
    
        while row < rows and col >= 0:
            if mat[row][col] == x:
                return True
    
            elif mat[row][col] >x:
                col -= 1
    
            else:
                row += 1
    
        return False
        	
