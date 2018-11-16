from NewAVLTreeMap import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap

if __name__ == "__main__":
    print("TEST NewAVLTreeMap\n")
    tree_new_avl = NewAVLTreeMap()
    tree_new_avl[5] = 6
    tree_new_avl[10] = 6
    tree_new_avl[8] = 6
    tree_new_avl[23] = 6
    tree_new_avl[6] = 6
    tree_new_avl[11] = 6
    tree_new_avl[15] = 6
    tree_new_avl[16] = 6
    tree_new_avl[18] = 6
    tree_new_avl[25] = 6
    tree_new_avl[1] = 6
    tree_new_avl[4] = 6

    tree_avl = AVLTreeMap()
    tree_avl[5] = 6
    tree_avl[10] = 6
    tree_avl[8] = 6
    tree_avl[23] = 6
    tree_avl[6] = 6
    tree_avl[11] = 6
    tree_avl[15] = 6
    tree_avl[16] = 6
    tree_avl[18] = 6
    tree_avl[25] = 6
    tree_avl[1] = 6
    tree_avl[4] = 6

    print("La stampa è fatta con la PreOrder per comprendere la disposizione dei nodi\n")
    print("Prima riga: NewAVLTree\nSeconda riga: AVLTree di TDPCollections\n")

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    del(tree_new_avl[16])
    del(tree_avl[16])
    print("\n\nElimino 16\n")

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 5\n")

    del(tree_new_avl[5])
    del (tree_avl[5])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 8\n")

    del(tree_new_avl[8])
    del (tree_avl[8])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 23\n")

    del(tree_new_avl[23])
    del (tree_avl[23])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 1\n")

    del(tree_new_avl[1])
    del (tree_avl[1])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 25\n")

    del(tree_new_avl[25])
    del (tree_avl[25])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 10\n")

    del(tree_new_avl[10])
    del (tree_avl[10])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 4\n")

    del(tree_new_avl[4])
    del (tree_avl[4])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 6\n")

    del(tree_new_avl[6])
    del (tree_avl[6])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 18\n")

    del(tree_new_avl[18])
    del (tree_avl[18])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 15\n")

    del(tree_new_avl[15])
    del (tree_avl[15])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nElimino 11\n")

    del(tree_new_avl[11])
    del (tree_avl[11])

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\nAlberi Vuoti!\nInizio a riempirli")

    tree_new_avl[11] = 6
    tree_avl[11] = 6

    print("\n\nAggiungo 11\n")

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 6\n")
    tree_new_avl[6] = 6
    tree_avl[6] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 4\n")
    tree_new_avl[4] = 6
    tree_avl[4] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 18\n")
    tree_new_avl[18] = 6
    tree_avl[18] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 22\n")
    tree_new_avl[22] = 6
    tree_avl[22] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 9\n")
    tree_new_avl[9] = 6
    tree_avl[9] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")

    print("\n\nAggiungo 25\n")
    tree_new_avl[25] = 6
    tree_avl[25] = 6

    for e in tree_new_avl.preorder():
        print(e.key(), end=" ")

    print("")

    for e in tree_avl.preorder():
        print(e.key(), end=" ")