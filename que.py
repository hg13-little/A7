# que.py
# A First In First Out (FIFO) queue
# Modified by:
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection


class Queue(SequentialCollection):
  
    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._data.pop(0)

    def peek(self):
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._data[0]
    pass
