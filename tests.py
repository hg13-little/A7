# tests.py
# Tests of Stack and Queue
# Please exercise them enough to
# show they work under different combinations
# of operations and different orders of those operations
# Modified by: 
import unittest
from stack import Stack
from que import Queue


class TestStack(unittest.TestCase):
    def test_stack_with_ints(self):
        s = Stack()

        s.push(42)
        s.push(7)
        s.push(93)
        s.push(15)
        s.push(68)
        s.push(21)

        self.assertEqual(len(s), 6)
        self.assertEqual(s.peek(), 21)
        self.assertEqual(s.pop(), 21)
        self.assertEqual(s.pop(), 68)
        self.assertEqual(s.pop(), 15)
        self.assertEqual(s.peek(), 93)
        self.assertEqual(s.pop(), 93)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 42)

        self.assertTrue(s.is_empty)
        pass

    def test_stack_with_strings(self):
        s = Stack()

        s.push("pizza")
        s.push("computer")
        s.push("basketball")
        s.push("mountain")
        s.push("football")
        s.push("music")

        self.assertEqual(s.peek(), "music")
        self.assertEqual(s.pop(), "music")
        self.assertEqual(s.pop(), "football")
        self.assertEqual(s.peek(), "mountain")
        self.assertEqual(s.pop(), "mountain")
        self.assertEqual(s.pop(), "basketball")
        self.assertEqual(s.pop(), "computer")
        self.assertEqual(s.pop(), "pizza")

        self.assertTrue(s.is_empty)
        pass


class TestQueue(unittest.TestCase):

    def test_queue_with_ints(self):
        q = Queue()

        q.push(84)
        q.push(13)
        q.push(57)
        q.push(99)
        q.push(26)
        q.push(41)

        self.assertEqual(len(q), 6)
        self.assertEqual(q.peek(), 84)
        self.assertEqual(q.pop(), 84)
        self.assertEqual(q.pop(), 13)
        self.assertEqual(q.pop(), 57)
        self.assertEqual(q.peek(), 99)
        self.assertEqual(q.pop(), 99)
        self.assertEqual(q.pop(), 26)
        self.assertEqual(q.pop(), 41)

        self.assertTrue(q.is_empty)

        pass

    def test_queue_with_strings(self):
        q = Queue()

        q.push("dog")
        q.push("school")
        q.push("coffee")
        q.push("gaming")
        q.push("summer")
        q.push("movie")

        self.assertEqual(q.peek(), "dog")
        self.assertEqual(q.pop(), "dog")
        self.assertEqual(q.pop(), "school")
        self.assertEqual(q.peek(), "coffee")
        self.assertEqual(q.pop(), "coffee")
        self.assertEqual(q.pop(), "gaming")
        self.assertEqual(q.pop(), "summer")
        self.assertEqual(q.pop(), "movie")

        self.assertTrue(q.is_empty)

        pass


if __name__ == '__main__':
    unittest.main()
