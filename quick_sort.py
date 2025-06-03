def partition(arr,l,h):
    pivot=arr[l]
    i=l
    j=h
    while i<j:
        while i<h and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[j]=arr[j],arr[l]
    return j


def quick_sort(arr,l,h):
    if l<h:
        j=partition(arr,l,h)
        quick_sort(arr,l,j-1)
        quick_sort(arr,j+1,h)
    return arr

# Test cases
def test_case(arr, expected):
    result = quick_sort(arr, 0, len(arr) - 1)
    print(f"Input: arr = {arr}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print("✅ Passed" if result == expected else "❌ Failed")
    print("-" * 50)

if __name__ == "__main__":
    test_case([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10])
    test_case([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    test_case([1], [1])
    test_case([], [])
    test_case([2, 2, 2], [2, 2, 2])