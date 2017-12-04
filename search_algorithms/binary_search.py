def binary_search(arr, n, src):
    
    low = 0
    high = n

    while True:

        if high < low:
            return -1

        mid = low + int((high-low)/2)

        if arr[mid] < src:
            low = mid+1

        elif arr[mid] > src:
            high = mid-1

        else:
            return mid

a = [2,3,5,9,11,14,16,17,19,22,23,24,29,31]

print(binary_search(a, 14, 2))
