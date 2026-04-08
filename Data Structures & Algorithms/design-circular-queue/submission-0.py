class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:
    # insert at the tail, remove from the head
    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        # this node will always stay at the front
        self.head = Node(-1)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.size < self.cap:
            # as exected
            self.tail.next = Node(value, self.head.next)
            self.tail = self.tail.next
            self.size += 1
            return True
        # if full
        return False

    def deQueue(self) -> bool:
        if self.size > 0:
            if self.size == 1:
                self.head.next = None
            else:
                self.head.next = self.head.next.next
            self.size -= 1
            return True
        # no elements 
        return False
        

    def Front(self) -> int:
        # head
        if not self.size:
            return -1
        return self.head.next.val


    def Rear(self) -> int:
        # tail
        if not self.size:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()