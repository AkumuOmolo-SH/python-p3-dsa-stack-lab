class Stack:
    def __init__(self, items=None, limit=100):
        # If no items are given, start with an empty list
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        # True if the stack has no items
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top only if not full
        if not self.full():
            self.items.append(item)

    def pop(self):
        # Remove and return the top item
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        # Look at the top item without removing it
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        # Return how many items are in the stack
        return len(self.items)

    def full(self):
        # True if the stack has reached the limit
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Search from the top of the stack.
        Top of stack is position 0, next is 1, and so on.
        Return -1 if not found.
        """
        # Start counting from the top (end of the list)
        position = 0
        for item in reversed(self.items):
            if item == target:
                return position
            position += 1
        return -1
