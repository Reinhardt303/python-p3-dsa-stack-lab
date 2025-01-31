class Stack:

    def __init__(self, items = [], limit = 100): 
        
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0


    def push(self, item):
            if len(self.items) < self.limit:
                self.items.append(item)
            else:
                OverflowError("Stack is full")

    def pop(self):
        if self.isEmpty():
            return None  # Check if the stack is not empty
              # Remove the last item
        else: return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):

         return len(self.items) >= self.limit

    def search(self, target):
        reversed_items = list(reversed(self.items))  # Reverse the stack to treat the top as the first element
        try:
            # Find the index of the target in the reversed list
            return reversed_items.index(target)
        except ValueError:
            return -1

