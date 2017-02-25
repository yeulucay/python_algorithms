"""
- O(n**2) worst case time complexity

- Find the smallest item in list and put it to the first sequence. Scan the rest in linear manner

- In place sort
"""

def selection_sort(list):
    n = len(list)

    for i in range(0, n-1):
        min = i

        for j in range(i+1, n):

            if list[j] < list[min]:
                min = j

        
        list[i], list[min] = list[min], list[i]

    return list

a = [14, 16, 11, 9, 34, 10 , 13, 14]

print(selection_sort(a))
