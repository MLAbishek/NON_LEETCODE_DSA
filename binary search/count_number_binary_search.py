from typing import List


def count_occurrences(arr: List[int], x: int) -> int:
    first = 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            first += 1
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    last = 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            last += 1
            l = mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return first + last


# Test cases
def test_case(arr, x, expected):
    result = count_occurrences(arr, x)
    print(f"Input: x = {x}, arr = {arr}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print("✅ Passed" if result == expected else "❌ Failed")
    print("-" * 50)


if __name__ == "__main__":
    test_case([2, 2, 3, 3, 3, 3, 4], 3, 4)
    test_case([1, 1, 2, 2, 2, 2, 2, 3], 2, 5)
    test_case([1, 1, 1, 1, 1], 1, 5)
    test_case([1, 2, 3, 4, 5], 6, 0)
