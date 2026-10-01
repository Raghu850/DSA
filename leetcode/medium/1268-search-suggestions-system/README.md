# Search Suggestions System

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array of strings `products` and a string `searchWord`.

Design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with `searchWord`. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return  *a list of lists of the suggested products after each character of* `searchWord` *is typed*.

 

 **Example 1:** 

```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

```

 **Example 2:** 

```
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

```

 

 **Constraints:** 

- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 104
- All the strings of products are unique.
- products[i] consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 14 ms (beats 67.65%)  
**Memory:** 22 MB (beats 94.29%)  
**Submitted:** 2026-10-01T13:36:55.993Z  

```py
class Solution:
    def suggestedProducts(self, prods: List[str], word: str) -> List[List[str]]:
        prods.sort()

        prefix: str = ""
        ans: list[list[str]] = []

        for i in range(0, len(word)):
            prefix += word[i]
            top_3_prods: list[str] = self.search_top_3(prefix, prods)
            ans.append(top_3_prods)

        return ans

    # mobile, moneypot, monitor, mouse, mousepad
    def search_top_3(self, prefix: str, prods: list[str]) -> list[str]:
        start: int = 0
        end: int = len(prods) - 1
        idx: int = 0

        while start <= end:
            mid: int = start + (end - start) // 2

            mid_prefix: str = prods[mid][0: len(prefix)]
            if mid_prefix >= prefix:
                idx = mid
                end = mid - 1
            elif mid_prefix < prefix:
                start = mid + 1

        common_prefixs: list[str] = []
        cnt: int = 0
        while idx < len(prods) and cnt < 3:
            if prefix == prods[idx][0: len(prefix)]:
                common_prefixs.append(prods[idx])
            else:
                break

            cnt += 1
            idx += 1

        return common_prefixs
```

---

[View on LeetCode](https://leetcode.com/problems/search-suggestions-system/)