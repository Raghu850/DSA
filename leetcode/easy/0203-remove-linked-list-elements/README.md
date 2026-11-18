# Remove Linked List Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return  *the new head*.

 

 **Example 1:** 

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

```

 **Example 2:** 

```
Input: head = [], val = 1
Output: []

```

 **Example 3:** 

```
Input: head = [7,7,7,7], val = 7
Output: []

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= val <= 50

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 9.21%)  
**Memory:** 22.3 MB (beats 70.55%)  
**Submitted:** 2026-11-17T13:02:43.819Z  

```py

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
```

---

[View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)