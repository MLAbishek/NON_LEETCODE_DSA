def doubleit(num):
    if num == 0:
        return 0
    doubleit(num // 10)
    print((num % 10) * 2, end="")


doubleit(12345)
