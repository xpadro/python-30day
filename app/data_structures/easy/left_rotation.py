
def rotate(arr, rotation):
    for i in range(rotation):
        arr.append(arr.pop(0))
    
    return arr

if __name__ == '__main__':
    rotation = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = rotate(arr, rotation)
    print(' '.join(map(str, result)))