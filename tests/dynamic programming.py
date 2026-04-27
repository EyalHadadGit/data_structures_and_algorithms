from algorithms.dynamic_programming.fibonacci import *
from algorithms.dynamic_programming.house_robber import *
from algorithms.dynamic_programming.lcs import *
from algorithms.dynamic_programming.edit_distance import *
from algorithms.dynamic_programming.number_factor import *
from algorithms.dynamic_programming.palindromes import *
from algorithms.dynamic_programming.knapsack import *
from algorithms.dynamic_programming.min_cost import *
from algorithms.dynamic_programming.egg_drop import *

# -----------------------
# TEST GROUPS
# -----------------------

def test_fibonacci():
    print("\nFibonacci:")
    n = 8
    assert fib_bottom_up(n) == fib_top_down(n, {}) == 21
    assert fib_bottom_up(0) == 0
    assert fib_bottom_up(1) == 1
    print("✔ passed")

def test_number_factor():
    print("\nNumber Factor:")
    n = 8
    assert number_factor_bottom_up(n) == number_factor_top_down(n, {}) == 25
    assert number_factor_bottom_up(0) == number_factor_top_down(0, {}) == 1
    print("✔ passed")

def test_house_robber():
    print("\nHouse Robber:")
    houses = [6, 7, 1, 30, 8, 2, 4]
    assert house_robber_bottom_up(houses) == house_robber_top_down(houses, 0, {}) == 41
    assert house_robber_bottom_up([]) == 0
    print("✔ passed")

def test_edit_distance():
    print("\nEdit Distance:")
    s1, s2 = "table", "tbrltt"
    assert edit_distance_bottom_up(s1, s2) == edit_distance_top_down(s1, s2, {}, 0, 0) == 4
    assert edit_distance_bottom_up("", "") == 0
    print("✔ passed")

def test_knapsack():
    print("\n0/1 Knapsack:")
    weights = [3, 1, 5, 2]
    values = [31, 26, 7, 0]
    capacity = 6
    bottom = zeroOneKnapsack_bottom_up(weights, values, capacity)
    top = zeroOneKnapsack_top_down(weights, values, capacity, {})
    assert bottom == top == 57
    print("✔ passed")

def test_lcs():
    print("\nLCS:")
    s1, s2 = "elephant", "erepat"
    bottom = longest_common_subsequence_bottom_up(s1, s2)
    top = longest_common_subsequence_top_down(s1, s2, {})
    assert bottom == top == 5
    print("✔ passed")

def test_egg_drop():
    print("\nEgg Drop:")
    assert egg_drop_bottom_up(0, 5) == 0
    assert egg_drop_bottom_up(5, 0) == float("inf")
    assert egg_drop_bottom_up(1, 10) == 1
    assert egg_drop_bottom_up(2, 2) == 2
    assert egg_drop_bottom_up(10, 10) == 4
    print("✔ passed")

def test_palindromes():
    print("\nPalindromes:")
    word = "elrmenmet"
    top = longest_palindromic_subsequence_top_down(word, 0, len(word) - 1, {})
    bottom = longest_palindromic_subsequence_bottom_up(word)
    assert top == bottom == 5
    print("✔ passed")

def test_min_cost():
    print("\nMin Cost to Cell:")
    matrix = [[i for i in range(10)] for _ in range(10)]
    top = min_cost_to_cell_top_down(matrix)
    bottom = min_cost_to_cell_bottom_up(matrix)
    assert top == bottom == 45
    print("✔ passed")

# -----------------------
# RUN ALL TESTS
# -----------------------

def run_all_tests():
    test_fibonacci()
    test_number_factor()
    test_house_robber()
    test_edit_distance()
    test_knapsack()
    test_lcs()
    test_egg_drop()
    test_palindromes()
    test_min_cost()
    print("\n🎉 ALL DP TESTS PASSED 🎉")

run_all_tests()