import time


class MinTopHeap:
    def __init__(self, init_list=None):
        # small top heap
        self.heap = []
        if init_list is not None:
            self.init_list = init_list
            self._build_heap_from_list()

    def _swap(self, idx_1, idx_2):  # idx starts from 0
        if not (0 <= idx_1 < len(self.heap) and 0 <= idx_2 < len(self.heap)):
            raise IndexError("Index out of range!")
        if not idx_1 == idx_2:
            temp = self.heap[idx_1]
            self.heap[idx_1] = self.heap[idx_2]
            self.heap[idx_2] = temp

    def _shift_up(self, i):  # i start from 1
        # ######## PROCESS ########
        # Step 1. while we do not reach the heap top, i.e. i/2 > 1
        # Step 2. choose the i-th element of the stack, compare with its parent heap[i/2] in which i/2 = floor(i/2)
        # Step 3. shift their values if child heap[i] < parent heap[i/2] then swap them, else run to Step 5
        # Step 4. i <- i/2, run to Step 1
        # Step 5. end
        while int(i/2) >= 1:
            if self.heap[i-1] < self.heap[int(i/2)-1]:
                self._swap(idx_1=i-1, idx_2=int(i/2)-1)
                i = int(i/2)
            else:
                break

    def _shift_down(self, i):  # i start from 1
        # ######## PROCESS ########
        # Step 1. while we do not reach the heap bottom, i.e. 2 * i < n, n = len(heap)
        # Step 2. choose the i-th element of the stack, get its smaller child T, T = 2*i if left is smaller else T = 2*i + 1
        # Step 3. shift their values if child heap[T] < parent heap[i] then swap them, else run to Step 5
        # Step 4. i <- T, run to Step 1
        # Step 5. end
        while 2 * i < len(self.heap) + 1:
            T = 2 * i  # T is 2*i (left-child) or 2*i + 1 (right-child), one with smaller value
            if T + 1 < len(self.heap) + 1 and self.heap[T+1-1] < self.heap[T-1]:
                T += 1
            if self.heap[T-1] < self.heap[i-1]:
                self._swap(idx_1=T-1, idx_2=i-1)
            else:
                break
            i = T  # inherit the index

    def push(self, element):
        # ######## PROCESS ########
        # Step 1. add the new element to the end of the heap
        # Step 2. shift up this new tail
        self.heap.append(element)
        self._shift_up(i=len(self.heap))

    def pop(self):
        # ######## PROCESS ########
        # Step 1. pop out the root and move the tail to this place
        # Step 2. shift down this new root
        if not self.heap:
            raise RuntimeError("You cannot pop a value from an empty heap!")
        if len(self.heap) == 1:
            return self.heap.pop()
        head = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._shift_down(i=1)
        return head

    def _build_heap_from_list(self):
        for element in self.init_list:
            self.push(element=element)

    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.pop())
        return sorted_list


if __name__ == '__main__':
    init_list = [8, 5, 2, 9, 3, 7, 1, 4, 6]
    heap = MinTopHeap(init_list=init_list)
    print(heap.heap)
    print(heap.heap_sort())


