from typing import List, Tuple

def find_floor_ceil(arr: List[int], x: int) -> Tuple[int, int]:
    l=0
    r=len(arr)-1
    floor=float('-inf')
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=x:
            floor=max(floor,arr[mid])
            l=mid+1
        else:
            r=mid-1
    
    if floor==float('-inf'):
        floor=-1
    
    l=0
    r=len(arr)-1
    ceil=float('inf')
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=x:
            ceil=min(ceil,arr[mid])
            r=mid-1
        else:
            l=mid+1
    
    if ceil==float('inf'):
        ceil=-1

    return (floor,ceil)


# Test cases
def test_case(arr, x, expected):
    result = find_floor_ceil(arr, x)
    print(f"Input: x = {x}, arr = {arr}")
    print(f"Expected: Floor = {expected[0]}, Ceil = {expected[1]}")
    print(f"Result:   Floor = {result[0]}, Ceil = {result[1]}")
    print("✅ Passed" if result == expected else "❌ Failed")
    print("-" * 50)

if __name__ == "__main__":
    test_case([3, 4, 4, 7, 8, 10], 5, (4, 7))
    test_case([3, 4, 4, 7, 8, 10], 8, (8, 8))
    test_case([1, 2, 4, 6, 10], 3, (2, 4))
    test_case([1, 2, 4, 6, 10], 11, (10, -1))
    test_case([1, 2, 4, 6, 10], 0, (-1, 1))
