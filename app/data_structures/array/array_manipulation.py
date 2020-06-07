def array_manipulation(n, queries):
    """ Starting with a 1-indexed n sized array, applies a list of queries, where each query is in the form:

        [start_index, end_index, amount_to_sum]
    
    For example, n=5 and queries = [[1, 3, 2], [3, 5, 7]]

        Starting array:             [0, 0, 0, 0, 0]
        Result after first query:   [2, 2, 2, 0, 0]
        Result after second query:  [2, 2, 9, 7, 7]
    
    After all queries are applied, return the maximum value in the array.

    
    Solution:

        In order to avoid O(N^2) complexity, it stores differences instead of the values. For example, having a result array 
        of 7 elements, for an input of [2, 4, 50], the result is:

            [0, 50, 0, 0, -50, 0, 0]

        Elements 3 and 4 have a value of 0, since this is the difference from the previous element value.

        The maximum value will be the sum of all the positive difference values.
    """


    result = []
    for _ in range(0, n):
        result.append(0)

    for query in queries:
        start, end, value = query[0], query[1], query[2]

        result[start-1] += value
        if end < len(result): result[end] -= value

    max_value = 0
    sum_positive_nums = 0

    for i in result:
        sum_positive_nums = sum_positive_nums + i
        
        if max_value < sum_positive_nums: max_value = sum_positive_nums
    
    return max_value


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)

    print(result)