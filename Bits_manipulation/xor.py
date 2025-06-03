arr = [4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6]
res = arr[0]
for i in range(1, len(arr)):
    res = res ^ arr[i]
res = bin(res)
zero_grp = []
one_grp = []
for j in arr:
    binary_val = bin(j)
    if binary_val[-2] == 0:
        zero_grp.append(int(binary_val, 2))
    else:
        one_grp.append(int(binary_val, 2))
ans_zero_grp = zero_grp[0]
for i in range(1, len(zero_grp)):
    
    ans_zero_grp = ans_zero_grp ^ bin(zero_grp[i])
ans_one_grp = one_grp[0]
for i in range(1, len(one_grp)):
    ans_one_grp = ans_one_grp ^ bin(one_grp[i])
print(ans_zero_grp, ans_one_grp)
