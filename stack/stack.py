"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        return False

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

# class LLStack:
#     def __init__(self):
#         self.size = 0
#         self.stack = LinkedList()
#     def __len__(self):
#         return self.size
#     def push(self, value):
#         self.size += 1
#         self.stack.add_to_head(value)
#     def pop(self):
#         self.size -= 1
#         return self.stack.remove_from_head()