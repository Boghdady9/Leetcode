# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        store=[]
        while head:
            store.append(head)
            head=head.next

        left,right=0,len(store)-1
        while left< right:
            store[left].next=store[right]
            left+=1
            if left==right:
                break
            store[right].next=store[left]
            right-=1
        store[left].next=None