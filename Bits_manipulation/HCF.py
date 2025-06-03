def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


ans = hcf(444, 24)
print(ans)
