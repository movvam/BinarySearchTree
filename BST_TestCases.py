import unittest
from binary_search_tree import *


class TestTreeNode(unittest.TestCase):
     def test_insert(self):
        print('Test insert in TreeNode')
        n1 = TreeNode(88)
        n1.insert(190)
        self.assertEqual(n1.key, 88 )
        self.assertEqual(n1.left, None )
        self.assertEqual(n1.right.key, 190 )
        self.assertEqual(n1.right.left, None )
    
     def test_findSuccessor(self): 
        print('Test Find Successor')
        n1 = TreeNode(12)
        n1.insert(24)
        n1.insert(6)
        n1.insert(10)
        n1.insert(4)
        n1.insert(9)
        n1.insert(7)
        n1.insert(20)
        self.assertEqual(n1.left.find_successor().key,7 )
        self.assertEqual(n1.find_successor().key,20 )
        print('Test Print Levels')
        n1.right.print_levels() 

     def test_findmin(self):
        print('Test find min')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(-8)
        t.insert(6)
        self.assertEqual(t.root.find_min(), -8 )
        self.assertEqual(t.root.right.find_min(),6)
         
     def test_findmax(self):
        print('Test find max')
        n1 = TreeNode(12)
        n1.insert(24)
        n1.insert(6)
        n1.insert(10)
        self.assertEqual(n1.find_max(), 24 )
        self.assertEqual(n1.left.find_max(), 10 )
        print('Test inorder Print')
        n1.inorder_print_tree()

class TestBST(unittest.TestCase):

    def test_insert(self):
        print('Test insert in BST')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(10)
        self.assertEqual(t.root.key, 5 )
        self.assertEqual(t.root.left.key, 2 )
        self.assertEqual(t.root.right.key, 10 )
        self.assertEqual(t.root.right.left, None )

    def test_is_empty(self): 
        print('Test is_empty')
        t = BinarySearchTree()
        self.assertTrue(t.is_empty())
        
    def test_find1(self):
        print('Test find in BST')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(-8)
        self.assertTrue(t.find(-8) )

    def test_find2(self):
        print('Test find in BST')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(-8)
        self.assertFalse(t.find(0) )
        print('Test print tree')
        t.print_tree()
      
    def test_delete_1(self):
        print('Test delete in BST 1')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(8)
        t.delete(5)
        self.assertEqual(t.root.key, 8 )

    def test_delete_2(self):
        print('Test delete in BST 2')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(8)
        t.delete(10)
        self.assertEqual(t.root.right.key, 8)

    def test_delete_3(self):
        print('Test delete in BST 3')
        t = BinarySearchTree()
        t.insert(5)
        t.insert(2)
        t.insert(10)
        t.insert(8)
        t.delete(2)
        self.assertEqual(t.root.left, None)
       
    
        

if __name__ == "__main__":
    unittest.main()
