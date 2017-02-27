"""
- O(n**2) worst case time complexity

- Suitable for large sized datasets

- Split array into two subarray by picking a pivot value. 
  arr1 contains smallers than pivot, arr2 contains biggers than pivot
"""

def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end

    done = False
    while not done:

        while not done:
            bottom = bottom+1

            if bottom == top:
                done = True
                break

            if list[bottom] > pivot:
                list[top] = list[bottom]
                break

        while not done:
            top = top-1

            if top == bottom:
                done = True
                break

            if list[top] < pivot:
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top


def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return

a = [10, 8, 12, 24, 33, 1, 51, 9, 41, 99, 45, 98, 15, 19, 21, 17, 30, 33, 41, 90]
start = 0
end = len(a)-1
quicksort(a, start, end)
print(a)



