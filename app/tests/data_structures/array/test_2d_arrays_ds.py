from data_structures.array.max_hour_glass import max_hour_glass

def test_max_hour_glass_sum():
    assert max_hour_glass([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]) == 19, "Should be 19"



