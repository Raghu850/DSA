class Solution:
    def minTime(self, arr, k):
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        def is_possible(max_time):
            painters = 1
            current_time = 0
            
            for time in arr:
                if current_time + time > max_time:
                    painters += 1
                    current_time = time
                    
                    if painters > k:
                        return False
                else:
                    current_time += time
            
            return True
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result