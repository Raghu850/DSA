class Solution:
    def findPages(self, arr, k):
        
        if k > len(arr):
            return -1
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        def is_possible(max_pages):
            students = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages > max_pages:
                    students += 1
                    current_pages = pages
                    
                    if students > k:
                        return False
                else:
                    current_pages += pages
            
            return True
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result