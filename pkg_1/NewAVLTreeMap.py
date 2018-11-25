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


    def _is_balanced(self, p):
        return -1 <= p._node._balance_factor <= 1

    def _rebalance_insert(self, p):
        if self.sibling(p) is not None:
            p = self.parent(p)
            p._node._balance_factor = 0
            p = None
        while p is not None:
            if not self._is_balanced(p):
                if p._node._balance_factor <= -2:
                    child = self.left(p)
                    if child._node._balance_factor <= 0:
                        p = self._restructure(self.left(child))
                        p._node._balance_factor = 0
                        child = self.right(p)
                        child._node._balance_factor = 0
                    else:
                        p = self._restructure(self.right(child))
                        if p._node._balance_factor < 0:
                            self.left(p)._node._balance_factor = 0
                            self.right(p)._node._balance_factor = 1
                        elif p._node._balance_factor == 0:
                            self.left(p)._node._balance_factor = 0
                            self.right(p)._node._balance_factor = 0
                        else:
                            self.left(p)._node._balance_factor = -1
                            self.right(p)._node._balance_factor = 0
                        p._node._balance_factor = 0

                elif p._node._balance_factor >= 2:
                    child = self.right(p)
                    if child._node._balance_factor >= 0:
                        p = self._restructure(self.right(child))
                        p._node._balance_factor = 0
                        child = self.left(p)
                        child._node._balance_factor = 0

                    else:
                        p = self._restructure(self.left(child))
                        if p._node._balance_factor > 0:
                            self.left(p)._node._balance_factor = -1
                            self.right(p)._node._balance_factor = 0
                        elif p._node._balance_factor == 0:
                            self.left(p)._node._balance_factor = 0
                            self.right(p)._node._balance_factor = 0
                        else:
                            self.left(p)._node._balance_factor = 0
                            self.right(p)._node._balance_factor = 1
                        p._node._balance_factor = 0
                p = None
            else:

                key = p.key()
                p = self.parent(p)
                if p is not None and p.key() > key:
                    p._node._balance_factor -= 1
                if p is not None and p.key() < key:
                    p._node._balance_factor += 1
                if p is not None and p._node._balance_factor == 0:
                    break

    def _rebalance_delete(self, p):
        if p is not None:
            if self.is_leaf(p):  # il padre del nodo eliminato è una foglia
                p._node._balance_factor = 0
                key = p.key()
                p = self.parent(p)
                if p is not None and p.key() > key:
                    p._node._balance_factor += 1
                if p is not None and p.key() < key:
                    p._node._balance_factor -= 1

            else:
                if self.right(p) is not None and self.left(p) is not None and self.is_leaf(
                        self.right(p)) and self.is_leaf(
                        self.left(p)):
                    p._node._balance_factor = 0
                if self.right(p) is not None and self.left(p) is not None and self.is_leaf(
                        self.right(p)) and not self.is_leaf(
                        self.left(p)):  # il padre del predecessore non ha nipoti a destra
                    p._node._balance_factor -= 1
                if self.right(p) is not None and self.left(p) is not None and self.is_leaf(
                        self.left(p)) and not self.is_leaf(
                        self.right(p)):  # il padre del predecessore non ha nipoti a destra
                    p._node._balance_factor += 1
                if (self.right(p) is not None or (self.right(p) is not None and self.left(
                        p) is not None)):  # il padre ha un figlio destro oppure entrambi
                    p._node._balance_factor += 1
                if self.left(p) is not None:  # il padre ha il figlio sinistro
                    p._node._balance_factor -= 1

            while p is not None:
                    if not self._is_balanced(p):
                        if p._node._balance_factor <= -2:
                            child = self.left(p)
                            if child._node._balance_factor <= 0:
                                p = self._restructure(self.left(child))
                                if p._node._balance_factor == 0:
                                    p._node._balance_factor = 1
                                    child = self.right(p)
                                    child._node._balance_factor = -1
                                else:
                                    p._node._balance_factor = 0
                                    child = self.right(p)
                                    child._node._balance_factor = 0
                            else:
                                p = self._restructure(self.right(child))
                                if p._node._balance_factor < 0:
                                    self.left(p)._node._balance_factor = 0
                                    self.right(p)._node._balance_factor = 1
                                elif p._node._balance_factor == 0:
                                    self.left(p)._node._balance_factor = 0
                                    self.right(p)._node._balance_factor = 0
                                else:
                                    self.left(p)._node._balance_factor = -1
                                    self.right(p)._node._balance_factor = 0
                                p._node._balance_factor = 0
                        elif p._node._balance_factor >= 2:
                            child = self.right(p)
                            if child._node._balance_factor >= 0:
                                p = self._restructure(self.right(child))
                                if p._node._balance_factor == 0:
                                    p._node._balance_factor = -1
                                    child = self.left(p)
                                    child._node._balance_factor = 1
                                else:
                                    p._node._balance_factor = 0
                                    child = self.left(p)
                                    child._node._balance_factor = 0
                            else:
                                p = self._restructure(self.left(child))
                                if p._node._balance_factor > 0:
                                    self.left(p)._node._balance_factor = -1
                                    self.right(p)._node._balance_factor = 0
                                elif p._node._balance_factor == 0:
                                    self.left(p)._node._balance_factor = 0
                                    self.right(p)._node._balance_factor = 0
                                else:
                                    self.left(p)._node._balance_factor = 0
                                    self.right(p)._node._balance_factor = 1
                                p._node._balance_factor = 0
                        key = p.key()
                        p = self.parent(p)
                        if p is not None and p.key() > key:
                            p._node._balance_factor += 1
                        if p is not None and p.key() < key:
                            p._node._balance_factor -= 1
                    else:
                        if  p._node._balance_factor == 1 or p._node._balance_factor == -1:
                            break
                        key = p.key()
                        p = self.parent(p)
                        if p is not None and p.key() > key:
                            p._node._balance_factor += 1
                        if p is not None and p.key() < key:
                            p._node._balance_factor -= 1
