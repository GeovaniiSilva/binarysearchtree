from unittest import TestCase
from .bst import BinarySearchTree


class TestBinarySearchTree(TestCase):
    """
        Class Test Binary Search Tree
    """

    def test_insert_node(self):
        """
            Method to test insert label
        """

        bst = BinarySearchTree()

        label = 8
        bst.insert(label=label)

        self.assertEqual(bst.empty(), False)
        self.assertEqual(bst.getRoot().getLabel(), label)