from arrays import selection_sort, linear_search_array, binary_search_array
from linked_list import linear_search_linked_list

# Creates a test for linear search on a linked list
def test_linear_search_linked_list():
    found = linear_search_linked_list()
    assert found == 5, "Test Failed: Expected index 5 for value 8"
    print("Test Passed: linear_search_linked_list")

# Creates a test for linear search on an array
def test_linear_search_array():
    array = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]
    found = linear_search_array(array, 8)
    assert found == 5, "Test Failed: Expected index 5 for value 8"
    print("Test Passed: linear_search_array")

# Creates a test for binary search on an array
def test_binary_search_array():
    array = [-4, 0, 1, 2, 3, 4, 7, 8, 9, 10]
    found = binary_search_array(array, 8)
    assert found == 7, "Test Failed: Expected index 7 for value 8"
    print("Test Passed: binary_search_array")

# Creates a test for selection sort on an array
def test_selection_sort():
    array = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]
    sorted_array = selection_sort(array)
    assert sorted_array == [-4, 0, 1, 2, 3, 4, 7, 8, 9, 10], "Test Failed: Expected [-4, 0, 1, 2, 3, 4, 7, 8, 9, 10]"
    print("Test Passed: selection_sort")
    



