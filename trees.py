class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None


new = Tree()
dat = Node(9)
new.root = dat
dat1 = Node(8)
dat.left = dat1
dat2 = Node(10)
dat.right = dat2
print(end=" ")
print(new.root.data)
print(new.root.left.data, end=" ")
print(new.root.right.data)
