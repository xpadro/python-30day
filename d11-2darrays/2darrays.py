

def max_hour_glass(arr):
    max_hour_glass = None

    for y in range(4):
        for x in range(4):
            current_hour_glass_sum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]

            if max_hour_glass is None or current_hour_glass_sum > max_hour_glass:
                max_hour_glass = current_hour_glass_sum
            
            print(str(arr[y][x]) + " " + str(arr[y][x+1]) + " " + str(arr[y][x+2]))
            print("   " + str(arr[y+1][x+1]))
            print(str(arr[y+2][x]) + " " + str(arr[y+2][x+1]) + " " + str(arr[y+2][x+2]))
            print("")
    
    return max_hour_glass



arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


''' Test matrix:
arr = [
    [1, 2, 3, 4, 5, 6], 
    [7, 8, 9, 10, 11, 12], 
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]]
'''

print(max_hour_glass(arr))