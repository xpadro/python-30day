from data_structures.queue.queue import Queue

def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.print() == [1, 2, 3], "Should be [1, 2, 3]"
    assert queue.size == 3, "Should be size of 3"

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1, "Should have dequeued 1"
    assert queue.size == 2, "Should be size of 2"
    assert queue.dequeue() == 2, "Should have dequeued 2"
    assert queue.size == 1, "Should be size of 1"
    assert queue.dequeue() == 3, "Should have dequeued 3"
    assert queue.size == 0, "Should be size of 0"
    assert queue.dequeue() == None, "Should have returned None"

def test_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.peek() == 1, "Should have popped 1"
    assert queue.size == 3, "Should be size of 3"
    assert queue.peek() == 1, "Should have popped 2"
    assert queue.size == 3, "Should be size of 3"