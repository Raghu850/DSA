class Solution:
    def kthElement(self, a, b, k):
        # code here
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        m = len(b)

        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            leftA = float('-inf') if cut1 == 0 else a[cut1 - 1]
            leftB = float('-inf') if cut2 == 0 else b[cut2 - 1]

            rightA = float('inf') if cut1 == n else a[cut1]
            rightB = float('inf') if cut2 == m else b[cut2]

            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            elif leftA > rightB:
                high = cut1 - 1

            else:
                low = cut1 + 1

        return -1