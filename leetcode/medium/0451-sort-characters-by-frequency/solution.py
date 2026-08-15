from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        buckets = [[] for _ in range(n + 1)]

        for char, count in freq.items():
            buckets[count].append(char)

        res = []

        for i in range(n, 0, -1):
            for char in sorted(buckets[i]):
                res.append(char * i)

        return ''.join(res)