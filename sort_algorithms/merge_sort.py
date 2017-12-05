"""
- O(n.log(n)) worst case time complexity

- divide and conquer
"""

def merge_func(l1, l2):

    c = []

    while (l1 is not None
        and l2 is not None
        and len(l1)>0
        and len(l2)>0):

        if l1[0] > l2[0]:
            c.append(l2.pop(0))
        else:
            c.append(l1.pop(0))

    while l1 is not None and len(l1) > 0:
        c.append(l1.pop(0))

    while l2 is not None and len(l2) > 0:
        c.append(l2.pop(0))

    return c

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = int(len(arr)/2)

    l1, l2 = arr[:mid], arr[mid:]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    
    return merge_func(l1, l2)

a = [10, 8, 4, 12, 3, 7, 4, 7, 9, 12, 11, 9, 10, 1, 18]
print(merge_sort(a))
