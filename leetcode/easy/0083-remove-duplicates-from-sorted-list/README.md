# Remove Duplicates from Sorted List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a sorted linked list,  *delete all duplicates such that each element appears only once*. Return  *the linked list  **sorted**  as well*.

 

 **Example 1:** 

```
Input: head = [1,1,2]
Output: [1,2]

```

 **Example 2:** 

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 78.67%)  
**Submitted:** 2026-11-20T16:32:18.084Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return head
        # temp=head
        # while temp!=None:
        #     runner=temp
        #     while runner.next!=None:
        #         if runner.next.val==temp.val:
        #             runner.next=runner.next.next
        #         else:
        #             runner=runner.next
        #     temp=temp.next
        # return head
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head
```

---

[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)