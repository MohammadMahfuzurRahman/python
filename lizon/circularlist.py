class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    # INSERT AT START
    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node
    # INSERT AT END
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    # INSERT AT MIDDLE / AFTER A VALUE
    def insert_middle(self, after_value, data):
        if self.head is None:
            return
        current = self.head
        while True:
            if current.data == after_value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break
    # DELETE FROM START
    def delete_start(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        self.head = self.head.next
        current.next = self.head
    # DELETE FROM END
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
    # DELETE FROM MIDDLE / DELETE A VALUE
    def delete_middle(self, value):
        if self.head is None:
            return
        # If deleting head
        if self.head.data == value:
            self.delete_start()
            return
        current = self.head
        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
    # DISPLAY
    def display(self):

        if self.head is None:
            print("Empty")
            return
        current = self.head
        while True:
            print(current.data, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")
# CREATE LIST
list1 = CircularLinkedList()
# Insert at end
list1.insert_end(10)
list1.insert_end(20)
list1.insert_end(30)
print("Original:")
list1.display()
# Start এ insert
list1.insert_start(5)
# Middle এ insert
# 20 এর পরে 25
list1.insert_middle(20, 25)
# End এ insert
list1.insert_end(40)
print("After Insertion:")
list1.display()
# Start থেকে delete
list1.delete_start()
# Middle থেকে delete
list1.delete_middle(25)
# End থেকে delete
list1.delete_end()
print("After Deletion:")
list1.display()