# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


head = [3,2,0,-4]
pos = 1
if not head:
    print('False')
slow=head
fast=head.next

while fast and fast.next:

    if fast==slow:
        return True
    slow=slow.next
    fast=fast.next.next
return False