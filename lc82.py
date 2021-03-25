class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(val=0, next=head)  # Note 1

        cur = dummy  # Note 2

        while cur.next and cur.next.next:
            # compare the next two elements
            if cur.next.val == cur.next.next.val:
                # duplicated, remove all the followings
                x = cur.next.val
                while cur.next.val == x:
                    cur.next = cur.next.next  # delete cur.next
                    if not cur.next:
                        return dummy.next
            else:
                cur = cur.next

        return dummy.next


"""
Note 1:
if the head might change, we can insert a dummy node to avoid complicated logic

Note 2:
Basic tricks, preserve the head with another variable and modify the link list. 

"""