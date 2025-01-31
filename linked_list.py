COUNTERS = {"steps": 0}

class Node:
# This class represents a node in the linked list.
# Each node contains data - the value of the node and 'next' - a pointer to the next node in the list.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
# This class represents the linked list. the node has data and the next node in the linked list.
# The linked list contains Node objects starting from the head node.

    def __init__(self):
    # The head pointer is initialized to None. This indicates that the list is empty at the beginning.
        self.head = None

    def insert(self, data):
    # Inserts a new node with the given data at the end of the list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

def linear_search_linked_list():
    # Creates a linked list and insert example data.
    linked_list = LinkedList()
    values = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]

    # Inserts each value into the linked list.
    for value in values:
        linked_list.insert(value)

    # Performs a linear search for the value .
    # If it finds the value of 8, it returns the number of steps -1, which is the index of item 8 in the linked list. If it doesn't find it it returns -1
    current = linked_list.head
    while current is not None:
        COUNTERS["steps"] += 1
        if current.data == 8:
            print(f"Value 8 found in linked list.")
            return COUNTERS["steps"] - 1
            break
        current = current.next # Moves to the next node
    return -1

    print("Linear search on linked list took {} steps".format(COUNTERS["steps"]))

if __name__ == "__main__":
    # Calls the linear_search_linked_list function when the script is executed
    linear_search_linked_list()