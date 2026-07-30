class Solution:
    def missingNum(self, arr):
        # code here
        i = 0
        while i < len(arr):
            a = arr[i] - 1
            if 0 <= a < len(arr) and arr[i] != arr[a]:
                arr[a], arr[i] = arr[i], arr[a]
            else:
                i += 1

        for j in range(len(arr)):
            if arr[j] != j + 1:
                return j + 1

        return len(arr) + 1