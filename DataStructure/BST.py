class Node(object):

    def __init__(self,value):
        self.r_child = None
        self.l_child = None
        self.value = value

class BST(object):

    def insert(self, root, node):

        if root is None:
            return node
        if root.value > node.value:
            root.l_child =self.insert(root.l_child, node)

        else:
            root.r_child = self.insert(root.r_child, node)

        return root

    def inorder(self, root):

        if not root:
            return None

        else:
            self.inorder(root.l_child)
            print(root.value)
            self.inorder(root.r_child)

    def preorder(self, root):

        if not root:
            return None

        else:
            print(root.value)
            self.preorder(root.l_child)
            self.preorder(root.r_child)
    
    def postorder(self, root):

        if not root:
            return None

        else:
            self.postorder(root.l_child)
            self.postorder(root.r_child)
            print(root.value)
    
r = Node(3)

binarystree = BST()

listt = [1,4,5,7,8,6,8,2]

for val in listt:
    binarystree.insert(r, Node(val))

print("--------inorder----------")
print(binarystree.inorder(r))
print("--------preorder----------")
print(binarystree.preorder(r))
print("--------postorder----------")
print(binarystree.postorder(r))
        
