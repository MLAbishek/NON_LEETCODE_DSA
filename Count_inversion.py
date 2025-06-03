def merge(arr,count):
    if len(arr)==1:
        return
    mid=len(arr)//2
    l=arr[:mid]
    r=arr[mid:]
    merge(l,count)
    merge(r,count)
    i=j=k=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            arr[k]=l[i]
            i+=1
        else:
            count[0]+=len(l)-i #counts the inversion
            arr[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        arr[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        arr[k]=r[j]
        j+=1
        k+=1
    
arr=[2, 4, 1, 3, 5]
count=[0]
merge(arr,count)
print(arr,count[0])
arr.sort()
sorted()