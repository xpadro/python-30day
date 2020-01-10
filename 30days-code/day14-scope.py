class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        '''
        Finds max difference between any of a's elements
        '''

        a.sort()
        first_el = a[0]
        last_el = a[len(a) - 1]

        self.maximumDifference = abs(first_el - last_el)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)