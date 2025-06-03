base = 16


def toBase(num):
    if num == 0:
        return
    toBase(num // base)
    rem = num % base
    hex = "0123456789ABCDEF"

    print(hex[rem], end="")


toBase(1484)
