# **Sorting and Searching Algorithms with Linked Lists and Arrays**

This project implements fundamental **sorting and searching algorithms** using both **arrays** and **linked lists**. The goal is to demonstrate **Selection Sort**, **Linear Search**, and **Binary Search**, while also comparing their behavior on different data structures. Additionally, the project includes unit tests to verify correctness.

---

## **Features**
- ✅ **Selection Sort**: Implements selection sort for arrays.
- ✅ **Linear Search**: Works on both arrays and linked lists.
- ✅ **Binary Search**: Works on sorted arrays.
- ✅ **Linked List Implementation**: A custom linked list is created using a `Node` class.
- ✅ **Performance Counters**: Tracks swaps for sorting and steps for searching.
- ✅ **Unit Testing**: Uses `pytest` to validate all implemented functions.

---

## **Implementation Details**
### **Array-Based Functions (`arrays.py`)**
- `selection_sort(arr)`: Sorts an array using **Selection Sort**.
- `linear_search_array(arr, target)`: Searches for an element using **Linear Search**.
- `binary_search_array(arr, target)`: Searches for an element in a **sorted array** using **Binary Search**.

### **Linked List-Based Functions (`linked_list.py`)**
- `Node` class: Represents a **single node** in the linked list.
- `LinkedList` class: Implements a **custom linked list** with insertion functionality.
- `linear_search_linked_list()`: Searches for an element using **Linear Search** in a linked list.

### **Testing (`test_linked_list.py`)**
- Tests **sorting and searching** functions on arrays.
- Tests **linear search** on the custom linked list.
- Uses assertions to verify correctness.

---
