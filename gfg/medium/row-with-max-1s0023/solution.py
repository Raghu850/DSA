class Solution:
    def rowWithMax1s(self, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0])

        max_ones = 0
        answer = -1

        for i in range(rows):
            low = 0
            high = cols - 1

            # Find first 1 using binary search
            while low <= high:
                mid = (low + high) // 2

                if mat[i][mid] == 1:
                    high = mid - 1
                else:
                    low = mid + 1

            # low = index of first 1
            ones = cols - low

            if ones > max_ones:
                max_ones = ones
                answer = i

        return answer