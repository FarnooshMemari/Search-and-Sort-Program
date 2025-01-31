# COUNTERS dictionary is used to track the number of swaps for selection sorting and steps during linear and binary searches.
COUNTERS = {"swaps": 0, "linear_search": 0, "binary_search": 0}

def selection_sort(arr):
    '''
    Performs selection sort on an array.
    Selection sort works by selecting the minimum element from the unsorted portion of the array 
    and swapping it with the first unsorted element, progressively moving through the array. 
    
    Parameters:
    The array to be sorted.
    
    Returns:
    The sorted array.
    
    COUNTERS["swaps"] tracks the number of swaps during the sorting.
    '''

    '''
    Big O Notation:
    Time complexity: O(n^2) due to the nested loops (one to iterate and one to find the minimum).
    Space complexity: O(1) because it sorts the array in place without using extra space.
    '''
    n = len(arr)
    # O(n^2)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            COUNTERS["swaps"] += 1
    return arr

def linear_search_array(arr, target):
    '''
    Performs a linear search in the array.
    Linear search iterates through the array  element by element, comparing each element 
    to the target value until finds the match or reaches the end of the array.
    
    Parameters:
    - The array to search.
    - The value we are searching for.
    
    Returns:
    - The index of the target value if found, otherwise -1.
    
    COUNTERS["linear_search"] tracks the number of steps taken during the search.
    '''
    COUNTERS["linear_search"] = 0
    # O(n)
    for i in range(len(arr)):
        COUNTERS["linear_search"] += 1
        if arr[i] == target:
            return i
    return -1

def binary_search_array(arr, target):
    '''
    Performs a binary search in a sorted array.
    Binary search works by repeatedly dividing the search interval in half. If the value of 
    the search key is less than the item in the middle of the interval, the search continues 
    in the lower part of the interval, otherwise in the upper part. the array should be already sorted.
    
    Parameters:
    - The sorted array to search.
    - The value we are searching for.
    
    Returns:
    - The index of the target value if found, otherwise -1.
    
    COUNTERS["binary_search"] tracks the number of steps during the search.
    '''
    COUNTERS["binary_search"] = 0
    left, right = 0, len(arr) - 1
    # O(log n)
    while left <= right:
        mid = (left + right) // 2
        COUNTERS["binary_search"] += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # Main function that tests the sorting and searching functions on our sample array.
    
    # Example array data
    array = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]

    # Linear search on unsorted array
    found = linear_search_array(array, 8)
    print("Linear search on array took {} steps".format(COUNTERS['linear_search']))
    print("Value found at index {}".format(found))

    # Sorts the array
    sorted_array = selection_sort(array)
    print("Sorting the array took {} swaps".format(COUNTERS['swaps']))

    # Binary search on sorted array
    found = binary_search_array(sorted_array, 8)
    print("Binary search on array took {} steps".format(COUNTERS['binary_search']))
    print("Value found at index {}".format(found))

if __name__ == "__main__":
    main()
