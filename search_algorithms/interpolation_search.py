def interpolation(arr, n, src):

    low = 0
    high = n-1
    mid = -1

    while True:

        if (low == high) or (arr[low] == arr[high]):
            return -1

        mid = low + int(((high-low)/(arr[high]-arr[low])) * (src - arr[low]))


        if arr[mid] < src:
            low = mid + 1
        elif arr[mid] > src:
            high = mid - 1
        else:
            return mid

a = [1,2,4,6,7,9,12,14,16,18,21,26,29,30,33,37]
print(interpolation(a, len(a), 21))

