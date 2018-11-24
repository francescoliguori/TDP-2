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

    # def _set_balance_factor(self, p):
    #     p._node._balance_factor = self._compute_height(
    #         self.right(p)) - self._compute_height(self.left(p))
    #
    # def _compute_height(self, p):
    #     if p is None:
    #         return 0
    #     else:
    #         left_depth = self._compute_height(self.left(p))
    #         right_depth = self._compute_height(self.right(p))
    #
    #         if left_depth > right_depth:
    #             return left_depth + 1
    #         else:
    #             return right_depth + 1

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
        # if self.right(p) is not None:
        #     p._node._balance_factor -= 1
        # elif self.left(p) is not None:
        #     p._node._balance_factor += 1
        # else:
        #     p._node._balance_factor = 0
        #rotate = False
        if p is not None:
            if self.is_leaf(p):  # il padre del nodo eliminato è una foglia
                p._node._balance_factor = 0
                key = p.key()
                p = self.parent(p)
                if p is not None and p.key() > key:
                    p._node._balance_factor += 1
                if p is not None and p.key() < key:
                    p._node._balance_factor -= 1
                # p = None
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
                        #rotate = True
                        key = p.key()
                        p = self.parent(p)
                        if p is not None and p.key() > key:
                            p._node._balance_factor += 1
                        if p is not None and p.key() < key:
                            p._node._balance_factor -= 1
                    else:
                        # if not rotate:
                        #     break
                        if  p._node._balance_factor == 1 or p._node._balance_factor == -1:
                            break
                        key = p.key()
                        p = self.parent(p)
                        if p is not None and p.key() > key:
                            p._node._balance_factor += 1
                        if p is not None and p.key() < key:
                            p._node._balance_factor -= 1

        #             # if not self._is_balanced(p):
                #     if p._node._balance_factor <= -2:
                #         child = self.left(p)
                #         if child._node._balance_factor <= 0:
                #             p = self._restructure(self.left(child))
                #             if child._node._balance_factor == 0:
                #                 p._node._balance_factor = -1
                #                 child = self.left(p)
                #                 child._node._balance_factor = 1
                #             else:
                #                 p._node._balance_factor = 0
                #                 child = self.right(p)
                #                 child._node._balance_factor = 0
                #         else:
                #             p = self._restructure(self.right(child))
                #             if p._node._balance_factor < 0:
                #                 self.left(p)._node._balance_factor = 0
                #                 self.right(p)._node._balance_factor = 1
                #             elif p._node._balance_factor == 0:
                #                 self.left(p)._node._balance_factor = 0
                #                 self.right(p)._node._balance_factor = 0
                #             else:
                #                 self.left(p)._node._balance_factor = -1
                #                 self.right(p)._node._balance_factor = 0
                #
                #     elif p._node._balance_factor >= 2:
                #         child = self.right(p)
                #         if child._node._balance_factor >= 0:
                #             p = self._restructure(self.right(child))
                #             if child._node._balance_factor == 0:
                #                 p._node._balance_factor = 1
                #                 child = self.right(p)
                #                 child._node._balance_factor = -1
                #             else:
                #                 p._node._balance_factor = 0
                #                 child = self.left(p)
                #                 child._node._balance_factor = 0
                #         else:
                #             p = self._restructure(self.left(child))
                #             if p._node._balance_factor > 0:
                #                 self.left(p)._node._balance_factor = -1
                #                 self.right(p)._node._balance_factor = 0
                #             elif p._node._balance_factor == 0:
                #                 self.left(p)._node._balance_factor = 0
                #                 self.right(p)._node._balance_factor = 0
                #             else:
                #                 self.left(p)._node._balance_factor = 0
                #                 self.right(p)._node._balance_factor = 1
                #     p = self.parent(p)




    #
    # # def _rebalance_delete(self, p):
    # #     self._rebalance(p)
    def _get_balance_factor(self, p):
        return p._node._balance_factor
    #
    # def _rebalance_insert(self, z):
    #     x = self.parent(z)
    #     while x is not None:
    #         if z == self.right(x):
    #             x._node._balance_factor += 1
    #             if self._get_balance_factor(x) > 0:
    #                 g = self.parent(x)
    #                 if self._get_balance_factor(z) < 0:
    #                     n = self._restructure(z) #doppia rotazione destra sinistra
    #                     if self._get_balance_factor(n) > 0:
    #                         x._node._balance_factor = -1
    #                         z._node._balance_factor = 0
    #                     elif self._get_balance_factor(n) == 0:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 0
    #                     else:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 1
    #
    #                     #inserire i fattori
    #                 else:
    #                     n = self._restructure(z) #singola rotazione sinistra
    #                     x._node._balance_factor = 0
    #                     z._node._balance_factor = 0
    #             else:
    #                 x._node._balance_factor -= 1
    #                 if self._get_balance_factor(x) < 0:
    #                     x._node._balance_factor = 0
    #                     x = None
    #                 else:
    #                     x._node._balance_factor = 1
    #                     z = x
    #         else:
    #             if self._get_balance_factor(x) < 0:
    #                 g = self.parent(x)
    #                 if self._get_balance_factor(z) > 0:
    #                     n = self._restructure(z) #doppia rotazione sinistra destra
    #                     if self._get_balance_factor(n) < 0:
    #                         x._node._balance_factor = -1
    #                         z._node._balance_factor = 0
    #                     elif self._get_balance_factor(n) == 0:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 0
    #                     else:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 1
    #                 else:
    #                     n = self._restructure(z) #destra
    #                     x._node._balance_factor = 0
    #                     z._node._balance_factor = 0
    #             else:
    #                 if self._get_balance_factor(x) > 0:
    #                     x._node._balance_factor = 0
    #                     x = None
    #                 else:
    #                     x._node._balance_factor = -1
    #                     z = x
    #         g = self.parent(n)
    #         if g is not None:
    #             if x == self.left(g):
    #                 g._node._left = n
    #             else:
    #                 g._node._right = n
    #             x = None
    #         else:
    #             n._node._parent = None


    # def _rebalance_delete(self, x):
    #
    #     while x is not None:
    #         b = None
    #         g = self.parent(x)
    #         if self.left(x) is None:
    #             if x._node._balance_factor > 0 and self.right(x) is not None:
    #                 z = self.right(x)
    #                 b = z._node._balance_factor
    #                 if b < 0:
    #                     n = self._restructure(self.left(z))
    #                    #right-left, y è la nostra n, quindi la onostr radice
    #                     if n._node._balance_factor > 0:
    #                         x._node._balance_factor = -1
    #                         z._node._balance_factor = 0
    #                     elif n._node._balance_factor == 0:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 0
    #                     else:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 1
    #                     n._node._balance_factor = 0
    #                 else:
    #                     n = self._restructure(self.right(z))
    #                     #rotate left, z è la nostra n
    #                     if n._node._balance_factor == 0:
    #                         x._node._balance_factor = 1
    #                         n._node._balance_factor = -1
    #                     else:
    #                         x._node._balance_factor = 0
    #                         n._node._balance_factor = 0
    #                 x = self.parent(x)
    #             else:
    #                 if x._node._balance_factor == 0:
    #                     x._node._balance_factor = 1
    #                     break
    #
    #                 x._node._balance_factor = 0
    #                 #x = self.parent(x)
    #
    #         else:
    #             if x._node._balance_factor < 0 and self.left(x) is not None:
    #                 z = self.left(x)
    #                 b = z._node._balance_factor
    #                 if b > 0:
    #                     #left-right
    #                     n = self._restructure(self.right(z))
    #                     if n._node._balance_factor > 0:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 1
    #                     elif n._node._balance_factor == 0:
    #                         x._node._balance_factor = 0
    #                         z._node._balance_factor = 0
    #                     else:
    #                         x._node._balance_factor = -1
    #                         z._node._balance_factor = 0
    #                     n._node._balance_factor = 0
    #
    #
    #                 else:
    #                     #right
    #                     n = self._restructure(self.left(z))
    #                     if n._node._balance_factor == 0:
    #                         x._node._balance_factor = -1
    #                         n._node._balance_factor = 1
    #                     else:
    #                         x._node._balance_factor = 0
    #                         n._node._balance_factor = 0
    #                 x = self.parent(x)
    #
    #             else:
    #                 if x._node._balance_factor == 0:
    #                     x._node._balance_factor = -1
    #                     break
    #
    #                 x._node._balance_factor = 0
    #                 #x = self.parent(x)
    #         #cioa
    #         x = self.parent(x)
    #         if x is not None:
    #             if b is not None and b == 0:
    #                 break
    #

def testing_insert_int(keys, values=6):
    tree_new_avl = NewAVLTreeMap()
    lista = keys.split(",")
    for i in range(len(lista)):
        tree_new_avl[int(lista[i])] = values
        print("\nInserisco key = ", lista[i])
        for e in tree_new_avl.preorder():
            print(e.key(), "balance: ", e._node._balance_factor)


def testing_insert_char(keys, values=6):
    tree_new_avl = NewAVLTreeMap()
    lista = keys.split(",")
    for i in range(len(lista)):
        tree_new_avl[lista[i]] = values
        print("\nInserisco key = ", lista[i])
        for e in tree_new_avl.preorder():
            print(e.key(), "balance: ", e._node._balance_factor)


if __name__ == "__main__":
    testing_insert_char("j,p,f,d,g,l,v,c,n,s,x,q,u")

    testing_insert_int("5,10,8,23,6,11,15,16,18,25,1,4")


    # print("")
    #
    # print("\n\nElimino 10\n")
    #
    # del(tree_new_avl[10])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
    #
    # print("")
    #
    # print("\n\nElimino 25\n")
    #
    # del(tree_new_avl[25])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
    # print("")
    #
    # # print("\n\nElimino 5\n")
    # # del(tree_new_avl[5])
    # #
    # # for e in tree_new_avl.preorder():
    # #     print(e.key(), "balance: ", e._node._balance_factor)
    #
    # print("\n\nElimino 16\n")
    # del(tree_new_avl[16])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
    #
    # print("\n\nElimino 18\n")
    # del(tree_new_avl[18])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
    #
    # print("\n\nElimino 11\n")
    # del(tree_new_avl[11])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
    #
    # print("\n\nElimino 4\n")
    # del(tree_new_avl[4])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)

    # print("\n\nElimino 25\n")
    # del(tree_new_avl[25])
    #
    # for e in tree_new_avl.preorder():
    #     print(e.key(), "balance: ", e._node._balance_factor)
