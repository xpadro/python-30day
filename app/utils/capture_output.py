import contextlib
from io import StringIO

def capture_stdout(func, args):
    temp_stdout = StringIO()

    with contextlib.redirect_stdout(temp_stdout):
        func(*args)
    
    output = temp_stdout.getvalue().strip()
    return output