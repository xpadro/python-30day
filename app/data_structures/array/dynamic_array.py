"""
Query: 1 x y
    - Find the sequence, seq, at index ((x XOR last_answer) % N) in seqList
    - Append y to sequence seq

Query: 2 x y
    - Find the sequence, seq, at index ((x XOR last_answer) % N) in seqList
    - Find the value of element (y % seq_size) in seq and assign it to last_answer
    - Print the new value of last_answer on a new line
"""
def dynamic_array(n, queries):
    seq = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for el in queries:
        query_num = el[0]
        x = el[1]
        y = el[2]

        index = (x ^ last_answer) % n

        if query_num == 1:
            seq[index].append(y)
        else:
            pos = y % len(seq[index])
            last_answer = seq[index][pos]
            result.append(last_answer)

    return result


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamic_array(n, queries)
    print(result)