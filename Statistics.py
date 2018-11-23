from NewAVLTreeMap import NewAVLTreeMap


class Statistics:

    def __init__(self, file_input):
        self.avl = NewAVLTreeMap()
        self._popola_albero(file_input)

    def _popola_albero(self, file_input):
        #  questa funzione popola l'albero con gli elementi del dataset. Se nella add non sarà necessario aggiornare il dataset allora si
        #  potrà rifinire ulteriormente il codice chiamando nel while line la funzione add
        with open(file_input, "r") as file:  # lo statement with ci chiude il file automaticamente
            line = file.readline()  # readline legge una riga volta per volta
            while line:  # fino a quando la riga non è none
                lista = line.split(" ")  #  prende gli elementi separati dallo spazio e li mette in una lista, i valori sono stringhe
                if len(lista) != 2:
                    raise ValueError("File Corrotto.")
                self.add(int(lista[0]), int(lista[1]))
                line = file.readline()  # passa alla riga successiva

    def add(self, k, v):
        if not isinstance(k, int) or not isinstance(v, int):
            raise TypeError("Il tipo di k e/o v non è valido")
        p = self.avl.find_position(k)  # controlla se la chiave è nell'albero
        if p is not None and p.key() == k:  # se p non ha trovato la chiave o ritorna None oppure il suo vicino(motivo della seconda condizione)
            self.avl[k][0] += 1  # aumenta di uno le occorrenze
            self.avl[k][1] += v  # somma a total il value
        else:
            self.avl[k] = [1, v]  # crea un nodo con occorrenza a 1 e total pari al valore

    def len(self):
        return len(self.avl)

    def _get_frequency(self, p):
        return p.value()[0]

    def _get_total(self, p):
        return p.value()[1]

    def occurrences(self):
        """Restituisce la somma delle frequenze di tutti gli elementi presenti nella mappa"""
        if self.len() == 0:
            raise Exception("Il dataset è vuoto")
        occorrenze = 0
        for p in self.avl.preorder():
            occorrenze += self._get_frequency(p)
            # occorrenze += e.value()[0]
        return occorrenze

    def average(self):
        """Restituisce la media dei valori di tutte le occorrenze presenti nel dataset"""
        # media dei valori = totale dei valori / totale delle occorrenze

        if self.len() == 0:
            raise Exception("Il dataset è vuoto")

        complessivo = 0
        for p in self.avl.preorder():
            complessivo += self._get_total(p)
        return complessivo/self.occurrences()

    def median(self):
        """ se il numero n di dati è dispari la mediana corrisponde al valore centrale,
            ovvero al valore che occupa la posizione ( n + 1 ) / 2.
            se il numero  n di dati è pari, la mediana è stimata utilizzando i due valori
            che occupano le posizioni ( n / 2 ) e ( ( n / 2 ) + 1 )
            :return: il valore della mediana"""
        # if self.len() == 0:
        #     raise Exception("Il dataset è vuoto")
        return self.percentile(50)

    def percentile(self, j=20):
        if self.len() == 0:
            raise Exception("Il dataset è vuoto")
        if not isinstance(j, int):
            raise TypeError("Il tipo di j non è valido")
        if j < 1 or j > 99:
            raise ValueError("Il valore di j non è valido")
        entries = 0
        for key in self.avl.keys():
            entries += self.avl[key][0]
        freq = 0
        for node in self.avl.inorder():
            freq += node.value()[0]
            if freq/entries >= j/100:
                return node.key()

    def mostFrequent(self, j):
        if self.len() == 0:
            raise Exception("Il dataset è vuoto")
        if not isinstance(j, int):
            raise TypeError("Il tipo di j non è valido")
        if j < 0 or j > self.len():
            raise ValueError("Il valore di j non è valido")

        dict_frequency = {}
        for e in self.avl.preorder():
            dict_frequency[e.key()] = e.value()[0]
        lista = sorted(dict_frequency, key=dict_frequency.__getitem__, reverse=True)
        return lista[0:j]
