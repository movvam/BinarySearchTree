# Name: Mani Movva
# Section: 7

"""This module contains a Node & pointer implementation."""

# Data definition: a BinarySearchTree is a class
class BinarySearchTree:

    def __init__(self):
        """creates a new TreeNode that is empty. It needs no parameters"""
        self.root = None                            # root is the highest value in a binary search tree

    # int -> nothing
    def insert(self, newkey):
        """inserts a new TreeNdode to the correct location. It requires a key(int) as an input"""
        if self.root is None:			    # if tree is empty
            self.root = TreeNode(newkey)
            return
        else:
            p = self.root
            if p.key > newkey:
                if p.left is None:
                    p.left = TreeNode(newkey)
                    p.left.parent = p
                else:
                    p.left.insert(newkey)
            else:
                if p.right is None:
                    p.right = TreeNode(newkey)
                    p.right.parent = p
                else:
                    p.right.insert(newkey)

    # int -> nothing
    def delete(self, key):
        """deletes the node containing key, assumes such a node exists. Requires a key(int) as an input."""
        if self.root is None:
            raise IndexError
        else:
            p = self.root
            if key < p.key and p.left is not None:
                p.left.delete(key)
            elif key > p.key and p.right is not None:
                p.right.delete(key)
            elif key == self.root.key:
                if p.left is None and p.right is None:
                    p.key = None
                    p = None                    
                elif p.left is None:
                    p.key = p.right.find_min(p.right)       # replaces the node with the maximum value from the right side, replaces keys to keep pointers
                    p.right.delete(p.key)       # removes the original location of the right side
                elif p.right is None:
                    p.key = p.left.find_max(p.left)
                    p.left.delete(p.key)
                else:
                    p.key = p.right.find_min(p.right)       # replaces the node with the maximum value from the right side, replaces keys to keep pointers
                    p.right.delete(p.key)       # removes the original location of the right side
    
    # int -> boolean
    def find (self, key):
        """Searches the Binary Search Tree for the input value. Returns true if the value exists in the tree, false otherwise"""
        p = self.root      # current node
        while p is not None and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right

        if p is None :
            return False	    
        else:
            return True     # might want to return the node or ???

    # nothing -> String
    def print_tree(self):
        """Prints out the values of TreeNodes in numeric order"""
        self.root.inorder_print_tree()            # print inorder the entire tree

    # nothing -> boolean
    def is_empty(self):  #          returns True if tree is empty, else False
        """Returns a boolean if the Binary Search Tree is empty or not"""
        if self.root is None:
            return True
        else:
             return False

   
# Data definition: a TreeNode is a class
class TreeNode:
    """Tree node: left and right child + data which can be any object"""

    def __init__(self, key, data=None, left=None, right=None, parent=None):
        """creates a new node that is empty. It needs parameter key"""

        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        self.level = 0

    # boiler plate
    def __repr__(self):
        return "%s" % (self.key)
        
    # int -> nothing
    def insert(self, key):
        """Insert new node with key, assumes data not present"""
        if self.key != None:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                    self.left.parent = self
                    self.left.level = self.level+1
                else:
                   self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                    self.right.parent = self
                    self.right.level = self.level+1
                else:
                    self.right.insert(key)
        else:
            self.key = key

        
    # nothing -> String
    def inorder_print_tree(self):                        # print inorder the subtree of self
        """Print tree content inorder"""

        if (self.left != None):
            self.left.inorder_print_tree()
            
        print(self.key, end=", ")
        
        if (self.right != None):
            self.right.inorder_print_tree()

        
    # int -> nothing
    def delete(self, key):
        """ Remove a key from the tree. Requires a key as an input parameter """
        if self is None:
            raise IndexError
        if key is None:
            return
        else:
            if key < self.key:
                self.left.delete(key)
            elif key > self.key:
                self.right.delete(key)
            elif key == self.key:
                if self.left is None and self.right is None:
                    if self == self.parent.left:
                        self.parent.left = None
                    else:
                        self.parent.right = None
                elif self.left is None:
                    self.key = self.right.find_min(self.right)        # replaces the node with the maximum value from the right side, replaces keys to keep pointers
                    self.right.delete(self.key)               # removes the original location of the right side
                elif self.right is None:
                    self.key = self.left.find_max(self.left)
                    self.left.delete(self.key)
                else:
                    self.key = self.right.find_min(self.right)       # replaces the node with the maximum value from the right side, replaces keys to keep pointers
                    self.right.delete(self.key)       # removes the original location of the right side
        
    # nothing,TreeNode -> int
    def find_min(self, tree = None):                
        """ Finds the TreeNode with the smallest value key below the (not required) input tree"""
        if tree is None:
            current = self
        else:
            current = tree
        minVal = current.key
        while current is not None and current.key is not None:
            if current.key < minVal:
                minVal = current.key
            current = current.left
        return minVal

    # nothing,TreeNode -> int
    def find_max(self, tree = None):                
        """ Finds the TreeNode with the largest value key below the (not required) input tree"""
        if tree is None:
            current = self
        else:
            current = tree
        maxVal = current.key
        while current is not None:
            if current.key > maxVal:
                maxVal = current.key
            current = current.right
        return maxVal

    # nothing -> TreeNode 
    def find_successor(self):   
        """returns the node that is the inorder successor of the node"""

        if self.right is not None:
            successorVal = self.right.key
            successor = self.right
            current = successor
            while current is not None:
                if current.key < successorVal:
                    successorVal = current.key
                    successor = current
                current = current.left
            return successor  
        elif self.right is None and self == self.parent.left:
            return self.parent
        elif self.right is None and self == self.parent.right:
            return self.parent.parent

    # nothing,int -> String
    def print_levels(self, levelOffset = None):  
        """inorder traversal prints list of pairs, [key, level of the node] where root is level 0"""
        if levelOffset is None:
            levelOffset = self.level
        if (self.left != None):
            self.left.print_levels(levelOffset)
            
            
        print("[%s, %s,]" %(self.key, self.level - levelOffset))
        
        if (self.right != None):
            self.right.print_levels(levelOffset)
            
        
