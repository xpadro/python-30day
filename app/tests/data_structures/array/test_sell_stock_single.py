from data_structures.array.sell_stock_single import sell

def test_sell_stock_single():
    assert sell([7,1,5,3,6,4]) == 5
    assert sell([1,2]) == 1
    assert sell([7,6,4,3,1]) == 0
    assert sell([7,2,5,3,1,6,4]) == 5
    assert sell([7,2,5,3,6,1,6,4]) == 5
    assert sell([1]) == 0
    assert sell([]) == 0
    assert sell([2,1]) == 0
    assert sell([1,2,3,4,1,5]) == 4
    assert sell([3,2,3,1,2,3,4,1,5]) == 4
    assert sell([3,2,3,1,2,3,4,3,5]) == 4
    assert sell([2,3,1]) == 1