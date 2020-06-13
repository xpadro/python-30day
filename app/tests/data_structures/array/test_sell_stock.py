from data_structures.array.sell_stock import sell

def test_sell_stock():
    assert sell([7,1,5,3,6,4]) == 7
    assert sell([1,2,3,4,5]) == 4
    assert sell([1,2]) == 1
    assert sell([7,6,4,3,1]) == 0