class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        xr = 0

        # XOR array elements and numbers 1 to n
        for i in range(n):
            xr = xr ^ arr[i]
            xr = xr ^ (i + 1)

        # Find rightmost set bit
        bitNo = 0
        while True:
            if xr & (1 << bitNo):
                break
            bitNo += 1

        zero = 0
        one = 0

        # Divide both array elements and 1..n into two groups
        for i in range(n):
            if arr[i] & (1 << bitNo):
                one = one ^ arr[i]
            else:
                zero = zero ^ arr[i]

            if (i + 1) & (1 << bitNo):
                one = one ^ (i + 1)
            else:
                zero = zero ^ (i + 1)

        # Check which one is repeating
        cnt = 0
        for x in arr:
            if x == zero:
                cnt += 1

        if cnt == 2:
            return [zero, one]

        return [one, zero]