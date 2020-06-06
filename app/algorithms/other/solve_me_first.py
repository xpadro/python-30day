""" compute the sum of two integers.

int solveMeFirst(int a, int b);

where,

	a is the first integer input.
	b is the second integer input
"""
def solveMeFirst(a,b):
	return a + b

if __name__ == '__main__':
	num1 = int(input())
	num2 = int(input())
	res = solveMeFirst(num1,num2)
	print(res)