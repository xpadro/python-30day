'''
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.

For example, given input strings = ['ab', 'ab', 'abc'] and queries = ['ab', 'abc', 'bc'], 
we find 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, we add an element to out return array, 
results = [2, 1, 0]
'''
def matching_strings(strings, queries):
    result = []

    for _ in queries:
        result.append(0)

    for i in range(len(strings)):
        for y in range(len(queries)):
            if strings[i] == queries[y]:
                result[y] = result[y] + 1
    
    return result

    
if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matching_strings(strings, queries)

    print('\n'.join(map(str, res)))
