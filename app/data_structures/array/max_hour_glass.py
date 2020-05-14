"""
Given a 6x6 2D array, it returns an integer, the maximum hourglass sum in the array.

We define an hourglass in a matrix arr to be a subset of values with indices falling in this pattern 
in arr's graphical representation:

a b c
  d
e f g
"""
def max_hour_glass(arr):
    max_sum = None

    for y in range(4):
        for x in range(4):
            current_sum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]

            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max_hour_glass(arr))