class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x

        data = x-self.min

        if data < 0:
            self.min = x

        self.stack.append(data)
        print("push:", self.stack)

    def pop(self) -> None:
        data = self.stack.pop()

        if data < 0:
            # return self.min
            self.min -= data

        if not self.stack:
            self.min = None

        print("pop:", self.stack)

    def top(self) -> int:
        print("top:", self.stack)
        data = self.stack[-1]
        if data < 0:
            return self.min
        return data + self.min

    def getMin(self) -> int:
        print("getMin:", self.stack)
        return self.min


if __name__ == "__main__":
    ms = MinStack()
    ms.push(2147483646)
    ms.push(2147483646)
    ms.push(2147483647)
    print(ms.top())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    ms.push(2147483647)
    print(ms.top())
    print(ms.getMin())
    ms.push(-2147483648)
    print(ms.top())
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
