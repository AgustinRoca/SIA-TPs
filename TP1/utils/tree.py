class Tree:
    def __init__(self, root_elem=None):
        self.root = Node(root_elem)

    def __iter__(self):
        yield from self._next(self.root)

    def find(self, elem):
        if self.root.elem == elem:
            return self.root
        else:
            return self.find_rec(self.root, elem)

    def find_rec(self, node, elem):
        if node is None:
            return None
        if node.elem == elem:
            return node
        for child in node.children:
            ans = self.find_rec(child, elem)
            if ans is not None:
                return ans
        return None

    def _next(self, curr):
        yield curr
        for child in curr.children:
            yield from self._next(child)


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.children = []
        self.parent = None

    def __eq__(self, elem):
        return self.elem == elem

    def __str__(self):
        return str(self.elem)

    def add_child(self, elem):
        if self.elem is None:
            self.elem = Node(elem)
        else:
            new_elem = Node(elem)
            new_elem.parent = self
            self.children.append(new_elem)








