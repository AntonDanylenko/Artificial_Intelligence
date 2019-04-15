class MyStack:
    def __init__(self, list = []):
        self.stack = list

    def __str__(self):
        return str(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop(len(self.stack)-1)


# def main():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)
#     stack.push(6)
#     stack.push(7)
#     stack.push(8)
#     stack.push(9)
#     print(stack)
#     print(stack.pop())
#     print(stack)
#
# main()
