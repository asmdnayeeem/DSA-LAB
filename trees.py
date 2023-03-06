class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    def insert(self, val):
        new = Node(val)
        root = self.root
        if root:
            while root:
                if val < root.data:
                    if root.left:
                        root = root.left
                    break
                elif val > root.data:
                    if root.right:
                        root = root.right
                    break
                elif val == root.data:
                    return
            if val < root.data:
                root.left = new
            elif val > root.data:
                root.right = new

        else:
            self.root = new

    def preorder(self):
        root = self.root
        def preorderin(root):
            if root:
                print(root.data, end=" ")
                preorderin(root.left)
                preorderin(root.right)
        print()
        preorderin(root)

    def inorder(self):
        root = self.root

        def inorderin(root):
            if root:
                inorderin(root.left)
                print(root.data, end=" ")
                inorderin(root.right)
        print()
        inorderin(root)

    def postorder(self):
        root = self.root

        def postorderin(root):
            if root:
                postorderin(root.left)
                postorderin(root.right)
                print(root.data, end=" ")
        print()
        postorderin(root)

    def max(self):
        root = self.root
        prev = None
        while root:
            prev = root
            root = root.right
        print()
        print(prev.data)

    def min(self):
        root = self.root
        prev = None
        while root:
            prev = root
            root = root.left
        print()
        print(prev.data)

    def search(self, val):
        root = self.root
        prev = None
        if root.data == val:
            return [root, root]
        try:
            while val != root.data:
                if val < root.data:
                    prev = root
                    root = root.left
                elif val > root.data:
                    prev = root
                    root = root.right
            return [root, prev]
        except AttributeError:
            print("Given number does not exist")

    def delete(self, val):
        nod = self.search(val)
        if nod[0].right == None and nod[0].left == None:
            nod[1].left = None
        elif nod[0].right == None or nod[0].left == None:
            if nod[0].right == None:
                nod[1].left = nod[0].left
            if nod[0].left == None:
                nod[1].right = nod[0].right
        elif nod[0].right != None and nod[0].left != None:
            prev = None
            if nod[0].right:
                prev = nod[0]
                n = nod[0].right
            while n.left:
                prev = n
                n = n.left
            nod[0].data = n.data
            prev.right = prev.right.right


if __name__ == "__main__":
    new = Tree()
    new.insert(9)
    new.insert(8)
    new.insert(10)
    new.insert(11)
    new.insert(7)
    new.preorder()
    new.inorder()
    new.postorder()
    new.max()
    new.min()
    new.search(11)
    new.delete(8)
    new.inorder()
    new.delete(9)
    new.inorder()
    new.preorder()
