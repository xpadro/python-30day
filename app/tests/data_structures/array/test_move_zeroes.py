from data_structures.array.move_zeroes import move_zeroes

def test_move_zeroes():
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0], "Should be [1,3,12,0,0]"