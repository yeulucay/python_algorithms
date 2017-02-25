"""
O(n**2) worst case time complexity
"""

def bubble_sort(list):
    loop = len(list)

    for i in range(loop - 1):
        swapped = False

        for j in range(loop - 1):

            if list[j] > list[j+1]:

                list[j], list[j+1] = list[j+1], list[j]

                swapped = True

        if not swapped:
            break

    return list

a = [3, 6, 1, 9, 12, 2, 1, 7]

print(bubble_sort(a))
