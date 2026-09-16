class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # INSERT AT START
    def insert_start(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
    # INSERT AT END
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
    # INSERT AT MIDDLE / AFTER A VALUE
    def insert_middle(self, after_value, data):
        current = self.head
        while current is not None:
            if current.data == after_value:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
    # DELETE FROM START
    def delete_start(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
    # DELETE FROM END
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None
    # DELETE FROM MIDDLE / DELETE A VALUE
    def delete_middle(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return
            current = current.next
    # DISPLAY
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("NULL")
# CREATE LIST
list1 = DoublyLinkedList()
# Insert at end
list1.insert_end(10)
list1.insert_end(20)
list1.insert_end(30)
print("Original:")
list1.display()
# Start এ insert
list1.insert_start(5)
# Middle এ insert (20 এর পরে 25)
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