class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return
        return self.items.pop()

    def peek(self):
        if self.items == []:
            return
        return self.items[len(self.items) - 1]

    def size(self):
        if self.items == []:
            return 0
        return len(self.items)