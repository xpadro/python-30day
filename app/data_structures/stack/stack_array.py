
class Stack:
    def __init__(self):
        self.array = []
        self.size = len(self.array)

    def push(self, value):
        self.array.append(value)
        self.size = self.size + 1


    def pop(self):
        if self.size == 0:
            return None
        
        result = self.array[self.size - 1]
        self.size = self.size - 1
        return result

    def peek(self):
        if self.size == 0:
            return None

        return self.array[self.size - 1]
    
    def print(self):
        return self.array[::-1]
