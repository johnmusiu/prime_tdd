"""
partition inputs:
number(int): -> 0 - infinity
    -> negatives :-> error
    -> small positives :-> 0, 1, 2, 3, 4, 5
    -> middle positive :->20, 30, 40, 50
    -> large numbers :-> 10000, 100000000

    0, -1 boundaries
    1000000000000000000000000000, edge case
    {}, "", (,) -> unexpected input
"""

# def test_negative(number=-20):
#     results = prime_tdd(number)
#     assert(results == "error")

# def test_small_positive_numbers(number=2):
#     results = prime_tdd(number)
#     assert(results == [2])

# def test_middle_positive(number=20):
#     results = prime_tdd(number)
#     assert(results == [2, 3, 5, 7, 11, 13, 17, 19])


# test_negative()
# test_small_positive_numbers()
# test_middle_positive()

# print("All tests pass")
from prime import prime_tdd
import unittest

class TestPrime(unittest.TestCase):
    def test_negative(self, number=-20):
        results = prime_tdd(number)
        assert(results == "error")

    def test_small_positive_numbers(self, number=2):
        results = prime_tdd(number)
        assert(results == [2])

    def test_middle_positive(self, number=20):
        results = prime_tdd(number)
        assert(results == [2, 3, 5, 7, 11, 13, 17, 19])
    
    # def test_large_numbers(self, number=1000):
    #     results = prime_tdd(number)
    #     assert(results == [])
    
    def test_unexpected_input(self, number="string"):
        results = prime_tdd(number)
        assert(results == "Unexpected non integer input")

if __name__ == '__main__':
    unittest.main()