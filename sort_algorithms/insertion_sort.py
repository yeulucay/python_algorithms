"""
- O(n**2) worst case time complexity

- not suitable for large datasets. 

-In place sort
"""

def insertion_sort(list):

    hole_postion = 0
    value_to_insert = 0

    for i in range(1, len(list)):
        
        value_to_insert = list[i]
        hole_position = i

        while hole_position > 0 and list[hole_position-1] > value_to_insert:
            list[hole_position] = list[hole_position-1]
            hole_position -= 1

        list[hole_position] = value_to_insert

    return list


a = [12, 3, 15, 11, 2, 5, 2, 12, 17]

print(insertion_sort(a))
