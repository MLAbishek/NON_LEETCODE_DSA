arr = [1, 5, 99, 8, 6, 2, 3, 6, 8, 9, 24, 52, 0, 34, 66]
for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]

        j -= 1
    arr[j + 1] = temp
print(arr)
