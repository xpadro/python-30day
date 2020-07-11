from algorithms.other.number_of_1_bits import hammingWeight

def test_hamming_weight():
    hammingWeight(0) == 0
    hammingWeight(1) == 1
    hammingWeight(2) == 2
    hammingWeight(3) == 2
    hammingWeight(8) == 1
    hammingWeight(11) == 3