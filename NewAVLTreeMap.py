from TdP_collections.map.binary_search_tree import TreeMap


class NewAVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing.

            We use convention that a "None" child has height 0, thus a leaf has height 1.
            """
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0  # will be recomputed during balancing

    def _set_balance_factor(self, p):
        p._node._balance_factor = self._compute_height(
            self.right(p)) - self._compute_height(self.left(p))

    def _compute_height(self, p):
        if p is None:
            return 0
        else:
            left_depth = self._compute_height(self.left(p))
            right_depth = self._compute_height(self.right(p))

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    def _is_balanced(self, p):
        return -1 <= p._node._balance_factor <= 1

    def _rebalance(self, p):
        while p is not None:
            self._set_balance_factor(p)
            if self._is_balanced(p):
                p = self.parent(p)
            else:
                if p._node._balance_factor <= -2:
                    child = self.left(p)
                    if child._node._balance_factor <= 0:
                        p = self._restructure(self.left(child))

                    else:
                        p = self._restructure(self.right(child))

                    self._set_balance_factor(p)
                    self._set_balance_factor(self.left(p))
                    self._set_balance_factor(self.right(p))

                elif p._node._balance_factor >= 2:
                    child = self.right(p)
                    if child._node._balance_factor >= 0:
                        p = self._restructure(self.right(child))

                    else:
                        p = self._restructure(self.left(child))
                    self._set_balance_factor(p)
                    self._set_balance_factor(self.left(p))
                    self._set_balance_factor(self.right(p))

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)




tree = NewAVLTreeMap()
tree[5] = 6
tree[10] = 6
tree[8] = 6
tree[23] = 6
tree[6] = 6
tree[11] = 6
tree[15] = 6
tree[16] = 6
tree[18] = 6
tree[25] = 6
tree[1] = 6
tree[4] = 6

for e in tree.preorder():
    print(e.key())

del(tree[16])
print("\n")
for e in tree.preorder():
    print(e.key())

del(tree[5])
print("\n")
for e in tree.preorder():
    print(e.key())

print("\n")
del(tree[8])

for e in tree.preorder():
    print(e.key())

print("\n")
del(tree[23])

for e in tree.preorder():
    print(e.key())

print("\n")
del(tree[1])

for e in tree.preorder():
    print(e.key())

del(tree[25])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[10])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[4])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[6])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[18])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[15])
print("\n")

for e in tree.preorder():
    print(e.key())

del(tree[11])
print("\n")

for e in tree.preorder():
    print(e.key())

tree[11] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[6] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[4] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[18] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[22] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[9] = 6
print("\n")

for e in tree.preorder():
    print(e.key())

tree[25] = 6
print("\n")

for e in tree.preorder():
    print(e.key())
# tree[9] = 6
# print("\n")
#
# for e in tree.preorder():
#     print(e.key())

# tree[23] = 6
# print("\n")
#
# for e in tree.preorder():
#     print(e.key())
