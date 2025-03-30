class Node:
    """A Node represents a semester record with roll number and CGPA."""
    def __init__(self, roll_number, cgpa):
        self.roll_number = roll_number
        self.cgpa = cgpa
        self.next = None  # Pointer to the next node

class LinkedList:
    """A Linked List to store and manage CGPA records."""
    def __init__(self):
        self.head = None  # Start of the linked list
        self.size = 0  # Track the number of semesters

    def add_node(self, roll_number, cgpa):
        """Adds a new semester record to the linked list."""
        new_node = Node(roll_number, cgpa)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1
        print(f"Semester {self.size} added: Roll No: {roll_number}, CGPA: {cgpa}")

    def search_node(self, index):
        """Finds and returns the CGPA for a given semester index (1-based)."""
        if index < 1 or index > self.size:
            print("Invalid index! Semester not found.")
            return None
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        print(f"Semester {index} -> Roll No: {temp.roll_number}, CGPA: {temp.cgpa}")
        return temp.cgpa

    def traverse(self):
        """Prints all stored semester records."""
        if not self.head:
            print("No CGPA records found!")
            return
        temp = self.head
        count = 1
        while temp:
            print(f"Semester {count}: Roll No: {temp.roll_number}, CGPA: {temp.cgpa}")
            temp = temp.next
            count += 1

    def get_size(self):
        """Returns the total number of semesters recorded."""
        print(f"Total semesters recorded: {self.size}")
        return self.size

# Example Usage
cgpa_list = LinkedList()

# Adding initial semesters
cgpa_list.add_node("CE101", 8.5)
cgpa_list.add_node("CE102", 9.0)

# Adding a new semester
cgpa_list.add_node("CE103", 8.8)

# Searching for a semester
cgpa_list.search_node(2)

# Traversing all records
cgpa_list.traverse()

# Getting the size of the list
cgpa_list.get_size()
