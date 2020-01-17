""" Return an array of two integers denoting the respective comparison points earned by a and b.

Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being 
Alice's score and the second being Bob's.

compareTriplets has the following parameter(s):

    a: an array of integers representing Alice's challenge rating
    b: an array of integers representing Bob's challenge rating
"""
def compare_triplets(a, b):
    points_a = 0
    points_b = 0

    for i, value in enumerate(a):
        if value > b[i]:
            points_a = points_a + 1
        elif value < b[i]:
            points_b = points_b + 1
    
    return [points_a, points_b]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = ' '.join(map(str, compare_triplets(a, b)))
    print(result)