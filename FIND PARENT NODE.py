class Node:
    def __init__(self,data):
        self.data = data
        self.rightNode = None
        self.leftNode = None
       
        
def findParent(node:Node,data:int,parent:int):
    if node is None:
        return
    
    if node.data == data:
        print(parent)
    else:
        findParent(node.leftNode,data,node.data)
        findParent(node.rightNode,data,node.data)
        
        
# Driver code
if __name__ == "__main__":
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    node = 3
    findParent(root, node, -1)