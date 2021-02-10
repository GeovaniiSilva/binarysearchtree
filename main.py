from bst import BinarySearchTree


if __name__ == "__main__":

    t = BinarySearchTree()

    labels = [8, 3, 1, 6, 4, 7, 10, 14, 13]

    for label in labels:
        t.insert(label=label)

    t.show(t.getRoot())