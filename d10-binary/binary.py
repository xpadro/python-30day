def binary(n):
    '''
    Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the 
    maximum number of consecutive 1's in n's binary representation.
    '''

    num = int(n)
    result = 0

    binary_num = int(bin(num)[2:])
    ones_arr = str(binary_num).split(sep="0")
  
    for i in ones_arr:
        length = int(len(i))
        
        if length > int(result):
            result = length
    
    return result


n = input()
print(binary(n))