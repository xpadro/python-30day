class BubbleSort:
    def sort(self, n, a):
        numberOfSwaps = 0

        for _ in range(n):
            for j in range(n-1):

                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    numberOfSwaps = numberOfSwaps + 1

            if numberOfSwaps == 0:
                break

        print(f"Array is sorted in {numberOfSwaps} swaps.")
        print(f"First Element: {a[0]}")
        print(f"Last Element: {a[n-1]}")


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
bubbleSort = BubbleSort()
bubbleSort.sort(n, a)

''' Print array
string_arr = [str(el) for el in a]
print(", " . join(string_arr))
'''