import contextlib
from io import StringIO

def capture_stdout(func, args):
    temp_stdout = StringIO()

    with contextlib.redirect_stdout(temp_stdout):
        func(*args)
    
    output = temp_stdout.getvalue().strip()
    return output

def build_list(node):
    result = []

    while node:
        result.append(node.data)

        node = node.next
    
    return result