from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def _removemin(self, node):
        if not node.left:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            temp = node
            node = temp.right
            while node.left:
                node = node.left
            node.right = self._removemin(temp.right)
            node.left = temp.left
        # update the size of the nodes
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    @staticmethod
    def _size(node):
        return node.size if node else 0


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.nodelists = []
        self.tree = tree
        self.traversalType = traversalType

        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.nodelists) == 0:
            raise StopIteration()
        return self.nodelists.pop(0)

    def preorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            self.nodelists.append(bst)
            _traverse(bst.left)
            _traverse(bst.right)

        if len(bst) > 0:
            _traverse(bst._root)

    def inorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            _traverse(bst.left)
            self.nodelists.append(bst)
            _traverse(bst.right)

        if len(bst) > 0:
            _traverse(bst._root)

    def postorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            _traverse(bst.left)
            _traverse(bst.right)
            self.nodelists.append(bst)

        if len(bst) > 0:
            _traverse(bst._root)


if __name__ == "__main__":
    print("====part A====")
    t = BSTTable()
    t.put(5, 'a')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'd')
    print(t._root)
    print()
    print(t._removemin(t._root))
    print()

    print("====part B====")
    t = BSTTable()
    t.put(5, 'a')
    t.put(1, 'b')
    t.put(2, 'c')
    t.put(0, 'd')
    print(t._remove(t._root, 5))
    print()
    print(t._remove(t._remove(t._root, 5), 1))
    print()

    try:
        print(t._remove(t._root, 10))
    except Exception as e:
        print(e)
    print()

    print("====part C====")
    input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
    bst = BSTTable()
    for key, val in input_array:
        bst.put(key, val)
    print("Preorder")
    traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    print()

    print("Inorder")
    traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    print()

    print("Postorder")
    traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
