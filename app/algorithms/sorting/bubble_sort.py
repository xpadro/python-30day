#O(n^2)
def sort(arr):
    index = len(arr)

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr


if __name__ == "__main__":
    result = sort([3, 5, 1, 15, 4, 7, 2])
    print(" ".join(map(str, result)))