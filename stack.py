# stack.py
# A Last In First Out (LIFO) stack
# Modified by:
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection

class Stack(SequentialCollection):
    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._data[-1]

    pass
