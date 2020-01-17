from other_problems.easy.a_very_big_sum import aVeryBigSum

def test_sum():
    assert aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015, "Should be 5000000015"