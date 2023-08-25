def binary_search_recursive(arr, target):
    def bin(l,r):
        if l > r:
            return -1

        middle = l + r // 2
        if target == arr[middle]:
            return middle
        elif arr[middle] < target:
            return bin(middle + 1,r)
        else:
            return bin(l,middle - 1)
    return bin(0, len(arr)-1)

print(binary_search_recursive([1, 3, 5, 7, 9], 5)) # 2
