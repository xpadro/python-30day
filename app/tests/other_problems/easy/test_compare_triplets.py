from other_problems.easy.compare_triplets import compare_triplets

def test_compare_triplets():
    assert compare_triplets([5, 6, 7], [3, 6, 10]) == [1, 1], "Should be [1, 1]"

