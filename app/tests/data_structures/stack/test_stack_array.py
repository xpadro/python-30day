from data_structures.stack.stack_array import Stack

def test_stack():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)

    assert stack.print() == [1, 2, 3], "Should be [1, 2, 3]"
    assert stack.size == 3, "Should be size of 3"

def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)

    assert stack.pop() == 1, "Should have popped 1"
    assert stack.size == 2, "Should be size of 2"
    assert stack.pop() == 2, "Should have popped 2"
    assert stack.size == 1, "Should be size of 1"
    assert stack.pop() == 3, "Should have popped 3"
    assert stack.size == 0, "Should be size of 0"
    assert stack.pop() == None, "Should have returned None"

def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)

    assert stack.peek() == 1, "Should have popped 1"
    assert stack.size == 3, "Should be size of 3"
    assert stack.peek() == 1, "Should have popped 2"
    assert stack.size == 3, "Should be size of 3"