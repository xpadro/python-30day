def diagonal_difference(arr):
    """ Given a square matrix, calculates the absolute difference between the sums of its diagonals.

    For example, the square matrix arr is shown below:

        1 2 3
        4 5 6
        9 8 9 

    Left-to-right diagonal: 1+5+9 = 15
    Right-to-left diagonal: 3+5+9 = 17
    Diagonal difference: |15 - 17| = 2

    """

    n = len(arr)
    j = n-1
    row = 0
    left_diagonal = []
    right_diagonal = []

    for i in range(n):
        left_diagonal.append(arr[i][row])
        right_diagonal.append(arr[j][row])
        row = row + 1
        j = j - 1

    return abs(sum(left_diagonal) - sum(right_diagonal))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)
    print(result)
