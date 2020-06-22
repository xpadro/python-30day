def pascal_triangle(num_rows: int):
    """ Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

    """


    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    
    result = [[1]]
    i = 1

    while i < num_rows:
        prev_row = result[i-1]
        result.append([1])
        curr_row = result[i]

        for j in range(len(prev_row)):
            if j < len(prev_row) - 1:
                left_op = prev_row[j]
                right_op = prev_row[j+1]
                curr_row.append(left_op + right_op)
        
        curr_row.append(1)
        i = i + 1
    
    return result

print(pascal_triangle(3))
