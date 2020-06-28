class Node:
  def __init__(self,val):
    self.left=None
    self.right=None
    self.v=val

root=Node(1)#                    |1|
root.left=Node(2)#              /   \  
root.right=Node(3)#           |2|   |3|
root.left.left=Node(4)#       / \
root.left.right=Node(5)#    |4| |5|
  
def inorder(root):#LEFT ROOT RIGHT
    if root:
      inorder(root.left)
      print(root.v,end=" ")
      inorder(root.right)

print("Inorder Traversal")
inorder(root)

def preorder(root):#ROOT LEFT RIGHT
    if root:
      print(root.v,end=" ")
      preorder(root.left)
      preorder(root.right)

print("\nPreorder Traversal")
preorder(root)

def postorder(root):#LEFT RIGHT ROOT 
    if root:
      postorder(root.left)
      postorder(root.right)
      print(root.v,end=" ")

print("\nPostorder Traversal")
postorder(root)
