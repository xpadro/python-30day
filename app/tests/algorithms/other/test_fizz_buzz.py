from algorithms.other.fizz_buzz import fizz_buzz

def test_fizz_buzz():
    assert fizz_buzz(1) == ["1"]
    assert fizz_buzz(2) == ["1", "2"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]