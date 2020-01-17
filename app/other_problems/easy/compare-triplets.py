
def compare_triplets(a, b):
    points_a = 0
    points_b = 0

    for i, value in enumerate(a):
        if value > b[i]:
            points_a = points_a + 1
        elif value < b[i]:
            points_b = points_b + 1
    
    return [points_a, points_b]


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

result = ' '.join(map(str, compare_triplets(a, b)))
print(result)