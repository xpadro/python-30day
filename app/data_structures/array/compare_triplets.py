def compare_triplets(a, b):
    """ Given two arrays, returns an array of two positions, where each position contains the points of each array,
    where each array gains a point every time it has a value higher than the other array.

    For example,

        a = [1, 4, 4, 3, 10]
        b = [1, 3, 6, 3, 15]

        result = [1, 2]

        Array 'b' won in two positions (3 and 5), while array 'a' won in one position (2)

    """


    points_a = 0
    points_b = 0

    for i, value in enumerate(a):
        if value > b[i]:
            points_a = points_a + 1
        elif value < b[i]:
            points_b = points_b + 1
    
    return [points_a, points_b]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = ' '.join(map(str, compare_triplets(a, b)))
    print(result)