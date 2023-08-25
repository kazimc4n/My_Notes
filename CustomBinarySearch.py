def binary(arr,target):
    def func(l,r):
        if r < l:
            return -1
        mid = (l + r) // 2

        if arr[mid] > target:
            return func(l, mid-1)
        elif arr[mid] == target:
            return mid
        else:
            return func(mid + 1, r)
    return func(0,len(arr)-1)
print(binary([1,2,3,4,5,10,12,15],15))