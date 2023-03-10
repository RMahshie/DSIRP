# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    


    # Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return


    # print function
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        
        if self.rightChild:
            self.rightChild.PrintTree()
        
        print(self.data)

    def search(self, value):
        if value == self.data:
            return str(value) + " is found in the BST"
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.search(value)
            else:
                return str(value) + " is not found in the BST"
        elif value > self.data:
            if self.rightChild:
                return self.rightChild.search(value)
            else:
                return str(value) + " is not found in the BST"

# Creating a root node
root = Node(27)
root.insert(14)
root.PrintTree()
#print(root.search(14))


def IsOperator(self, s):
 if '+' in s:
  return True
 if '-' in s:
  return True
 if '*' in s:
  return True
 if '/' in s:
  return True
 return False

multiply = 42
addition = 43
subtract = 45
division = 47
exponent = 94
openParenthese = 40
closeParenthese = 41
print(ord(")"))

