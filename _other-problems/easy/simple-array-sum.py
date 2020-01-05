def simpleArraySum(ar):
    #
    # Write your code here.
    #
    return sum(ar)


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)
print(result)