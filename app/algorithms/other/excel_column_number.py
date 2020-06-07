from string import ascii_lowercase

class ExcelColumn:
    def __init__(self):
        self.chars = {}
        index = 1
        
        for c in ascii_lowercase:
            self.chars[c] = index
            index = index + 1


    def resolve(self, column):
        """ Given the letters of the typical excel columns (A, AB, ...), return the value.

        For example:

            A: 1
            B: 2
            Z: 26
            AA: 27

        """

        result = 0

        for i, value in enumerate(reversed(column)):
            if i == 0:
                result = self.chars[value.lower()]
            else:
                result = result + (26 * i * self.chars[value.lower()])
        
        return result
