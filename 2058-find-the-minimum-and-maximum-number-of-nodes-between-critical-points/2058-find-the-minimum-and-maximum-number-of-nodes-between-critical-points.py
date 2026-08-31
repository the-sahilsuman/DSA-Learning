# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indices = []
        prev, curr = head, head.next
        idx = 1
        
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
            (curr.val < prev.val and curr.val < curr.next.val):
                indices.append(idx)
            prev = curr
            curr = curr.next
            idx += 1
            
        if len(indices) < 2:
            return [-1, -1]
            
        max_dist = indices[-1] - indices[0]
        min_dist = min(indices[i] - indices[i - 1] for i in range(1, len(indices)))
        
        return [min_dist, max_dist]