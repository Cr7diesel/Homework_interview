class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return f'{self.stack}'


if __name__ == '__main__':
    new_value = Stack()
    print(new_value.isEmpty())
    new_value.push(8)
    new_value.push(9)
    new_value.push(10)
    print(new_value)
    new_value.pop()
    print(new_value)
    print(new_value.peek())
    print(new_value.size())
    print(new_value.isEmpty())
