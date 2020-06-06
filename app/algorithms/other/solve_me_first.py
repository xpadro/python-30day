def solve_me_first(a,b):
	""" Compute the sum of two integers.

	int solve_me_first(int a, int b);

	where,

		a is the first integer input.
		b is the second integer input
		
	"""


	return a + b

if __name__ == '__main__':
	num1 = int(input())
	num2 = int(input())
	res = solve_me_first(num1,num2)
	print(res)