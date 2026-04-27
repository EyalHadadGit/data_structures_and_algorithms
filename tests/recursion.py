from techniques.recursion import *

def test_factorial():
    print("\nTesting factorial...")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
    try:
        factorial(-3)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✔ factorial passed")

def test_gcd():
    print("\nTesting gcd...")
    assert gcd(48, 18) == 6
    assert gcd(7, 3) == 1
    assert gcd(100, 10) == 10
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    print("✔ gcd passed")

def test_reverse():
    print("\nTesting reverse...")
    assert reverse("hello") == "olleh"
    assert reverse("a") == "a"
    assert reverse("") == ""
    try:
        reverse(123)
        assert False, "Should raise TypeError"
    except TypeError:
        pass
    print("✔ reverse passed")

def test_flatten():
    print("\nTesting flatten...")
    assert flatten([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[[1]]]) == [1]
    print("✔ flatten passed")

def test_nested_even_sum():
    print("\nTesting nested_even_sum...")
    data1 = {"a": 2, "b": {"c": 4, "d": 3}, "e": 5}
    data2 = {"x": 1, "y": {"z": 6, "w": {"k": 8}}}
    data3 = {}
    assert nested_even_sum(data1) == 6
    assert nested_even_sum(data2) == 14
    assert nested_even_sum(data3) == 0
    print("✔ nested_even_sum passed")

def run_all_tests():
    test_factorial()
    test_gcd()
    test_reverse()
    test_flatten()
    test_nested_even_sum()
    print("\n🎉 ALL RECURSION TESTS PASSED 🎉")

run_all_tests()