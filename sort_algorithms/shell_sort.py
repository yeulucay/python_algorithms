"""
- O(n) worst case time complexity

- Based on insertion sorted

- Efficient for medium size datasets
"""

def shell_sort(arr):

    inc = len(arr)//2

    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


A = [35, 33, 42, 10, 14, 19, 27, 44, 3, 4]
shell_sort(A)
print(A)

