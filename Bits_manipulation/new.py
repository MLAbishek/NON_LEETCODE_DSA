def op(num, shift):
    if (1 << shift) > num:
        return
    op(num, shift + 1)
    if num & (1 << shift):
        print(shift + 1, end=" ")


op(9, 0)
