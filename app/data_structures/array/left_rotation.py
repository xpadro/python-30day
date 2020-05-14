'''
Shifts array's elements n units to the left.

For example, given arr=[1, 2, 3, 4, 5] and n=2, then the result would be:

    [3, 4, 5, 1, 2]
'''
def rotate(arr, n):
    for i in range(n):
        arr.append(arr.pop(0))
    
    return arr

if __name__ == '__main__':
    rotation = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = rotate(arr, rotation)
    print(' '.join(map(str, result)))