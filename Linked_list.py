# ------------------------------------------
# Singly Linked List Implementation in Python
# ------------------------------------------

# Node class represents each element in the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class encapsulates all operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert a node after a given value
    def insert_after(self, target_data, data):
        current = self.head
        while current and current.data != target_data:
            current = current.next
        if not current:
            print(f"Node with value {target_data} not found!")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to delete is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the node wasn't found
        if not current:
            print(f"Node with value {key} not found!")
            return

        prev.next = current.next
        current = None

    # Search for a node by value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Display all nodes
    def display(self):
        current = self.head
        if not current:
            print("Linked List is empty!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ------------------------------------------
# Example Usage
# ------------------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.insert_after(20, 25)

    print("Linked List after insertions:")
    ll.display()

    # Delete a node
    ll.delete_node(10)
    print("\nAfter deleting 10:")
    ll.display()

    # Search in list
    print("\nSearching for 25:", ll.search(25))
    print("Searching for 100:", ll.search(100))
