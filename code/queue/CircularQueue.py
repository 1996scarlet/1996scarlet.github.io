class CircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        assert k > 0
        self.size = k
        self.queue = [None] * self.size
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.head] is not None:
            next_tail = (self.tail + 1) % self.size
            if self.queue[next_tail]:
                return False
            else:
                self.tail = next_tail

        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.head] is not None:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
            if self.queue[self.head] is None:
                self.head = 0
                self.tail = 0
            return True
        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.queue[self.head] is not None:
            return self.queue[self.head]

        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        print(self.queue, self.head, self.tail)
        if self.queue[self.tail] is not None:
            return self.queue[self.tail]
    
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail == 0 and self.queue[0] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1)%self.size == self.head


if __name__ == "__main__":
    obj = CircularQueue(8)
    print(obj.enQueue(3))
    print(obj.enQueue(9))
    print(obj.enQueue(5))
    print(obj.enQueue(0))
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.isEmpty())
    print(obj.isEmpty())
    print(obj.Rear())
    print(obj.Rear())
    print(obj.deQueue())

    # print(obj.isFull())
