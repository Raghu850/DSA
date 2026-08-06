class Solution:
    def inversionCount(self, arr):
        def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid + 1, right)

            i = left
            j = mid + 1
            temp = []

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])

                    # arr[i] > arr[j]
                    # So arr[i], arr[i+1], ..., arr[mid]
                    # are all greater than arr[j]
                    count += mid - i + 1

                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[left + k] = temp[k]

            return count

        return merge_sort(0, len(arr) - 1)