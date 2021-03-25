class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import Queue
class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        
        processors, successors = Queue(), Queue()
        idx = 0
        while head:
            if not idx // 2:
                processors.put(head)
            else:
                successors.put(head)
            head = head.next
            idx += 1

        head = processors.get()
        ret = head
        track = 1
        while idx - 1:
            if track // 2 and not successors.empty():
                head.next = successors.get()
            else:
                head.next = processors.get()
            head = head.next
            idx -= 1
            track += 1
        return ret


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        odds = []
        evens = []
        idx = 0
        while head:
            if not idx % 2:
                odds.append(head.val)
            else:
                evens.append(head.val)
            head = head.next
            idx += 1
        print(odds, evens)
        # reconstruct
        ret = ListNode(evens[0])
        node = ret
        rec = 1
        while rec < idx:
            if rec % 2:
                node.next = ListNode(odds[rec // 2])
            else:
                if rec // 2 == len(evens):
                    node.next = ListNode(odds[-1])
                    return ret
                node.next = ListNode(evens[rec // 2])
            node = node.next
            rec += 1

        return ret


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head

        return newhead

        

        


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ret = Solution().swapPairs(head)
    while ret:
        print(ret.val)
        ret = ret.next


### Notes:

"""
1. design the FORWARD part carefully when using recursion. For instance, in our intuition, 
we could easily imagine the function's goal, that is, swap right from the head. However, 
if we fomulates as:

            head.next = swap(head.next)     (1)

The process will then go out of control, since we expect the exchange like 21435 rather than
13254. Thus, the basic operation element is step 2, and only odd ones are starting points. 

            head <-> head.next
            head.next = swap(head.next.next)  (2)  # you might draw out this process

2. The BACKWARD of a recursion relies on its goal -> end criterion, it is local
   The FORWARD  of a recursion supposes we have realized the successors, the key point is how
to couple them. 
            
"""
