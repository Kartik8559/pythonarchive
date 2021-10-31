class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularLL:
    def __init__(self):
        self.head = None
        
    def insert_at_beg(self,data):
        new_node = Node(data)
        actual_node = self.head
        new_node.next = self.head
        
        if not self.head:
            new_node.next = new_node
        else:
            while actual_node.next != self.head:
                actual_node = actual_node.next
            actual_node.next = new_node
        self.head = new_node
        
    def insert_end(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            actual_node = self.head
            while actual_node.next != self.head: 
                actual_node = actual_node.next
            actual_node.next = new_node
        new_node.next = self.head
        
    def traverse(self):
        actual_node = self.head
        
        while actual_node:
            print(actual_node.data)
            actual_node = actual_node.next
            if actual_node == self.head:
                break
            
            
if __name__ == "__main__":
    yash = CircularLL()
    yash.insert_at_beg(1)
    yash.insert_at_beg(5)
    yash.insert_at_beg(2)
    yash.insert_at_beg(7)
    yash.insert_end(10)
    yash.insert_end(9)
    yash.insert_end(7)
    yash.traverse()