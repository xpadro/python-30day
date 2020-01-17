class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors_sum = 0
        current = n

        while current > 0:
            if n % current == 0:
                divisors_sum = divisors_sum + current
            
            current = current - 1

        return divisors_sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)