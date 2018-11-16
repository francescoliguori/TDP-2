from NewAVLTreeMap import NewAVLTreeMap


class Statistics:

    def __init__(self, file_input):
        self.avl = NewAVLTreeMap()
        self._file_input = file_input  # questo attributo lo teniamo nel caso in cui nel metodo add bisogna aggiornare il file (è un dubbio)
        # with open(file_input, "r") as file:  #lo statement with ci chiude il file automaticamente
        #     line = file.readline()  # readline legge una riga volta per volta
        #     while line:  # fino a quando la riga non è none
        #         lista = line.split(" ")  # prende gli elementi separati dallo spazio e li mette in una lista, i valori sono stringhe
        #         p = self.avl.find_position(int(lista[0]))  # controlla se la chiave è nell'albero
        #         if p is not None and p.key() == int(lista[0]): # se p non ha trovato la chiave o ritorna None oppure il suo vicino(motivo della seconda condizione)
        #             self.avl[int(lista[0])][0] += 1  # aumenta di uno le occorrenze
        #             self.avl[int(lista[0])][1] += int(lista[1])  #somma a total il value
        #         else:
        #             self.avl[int(lista[0])] = [1, int(lista[1])]  # crea un nodo con occorrenza a 1 e total pari al valore
        #         line = file.readline()  # passa alla riga successiva
        self._popola_albero(file_input)


    def _popola_albero(self,file_input):
        #questa funzione popola l'albero con gli elementi del dataset. Se nella add non sarà necessario agiornare il dataset allora si
        #potrà rifinire ulteriormente il codice chiamando nel while line la funzione add

        with open(file_input, "r") as file:  # lo statement with ci chiude il file automaticamente
            line = file.readline()  # readline legge una riga volta per volta
            while line:  # fino a quando la riga non è none
                lista = line.split(" ")  # prende gli elementi separati dallo spazio e li mette in una lista, i valori sono stringhe
                p = self.avl.find_position(int(lista[0]))  # controlla se la chiave è nell'albero
                if p is not None and p.key() == int(lista[0]):  # se p non ha trovato la chiave o ritorna None oppure il suo vicino(motivo della seconda condizione)
                    self.avl[int(lista[0])][0] += 1  # aumenta di uno le occorrenze
                    self.avl[int(lista[0])][1] += int(lista[1])  # somma a total il value
                else:
                    self.avl[int(lista[0])] = [1, int(lista[1])]  # crea un nodo con occorrenza a 1 e total pari al valore
                line = file.readline()  # passa alla riga successiva

    def add(self, k, v):
        p = self.avl.find_position(k)  # controlla se la chiave è nell'albero
        if p is not None and p.key() == k:  # se p non ha trovato la chiave o ritorna None oppure il suo vicino(motivo della seconda condizione)
            self.avl[k][0] += 1  # aumenta di uno le occorrenze
            self.avl[k][1] += v  # somma a total il value
        else:
            self.avl[k] = [1, v]  # crea un nodo con occorrenza a 1 e total pari al valore

        # questo codice aggiorna anche il file, come ho detto prima, credo che non si deve fare
        with open(self._file_input, 'a') as file:  # 'a' aggiorna il file scrivendo una nuova riga alla fine

            file.write("\n{} {}".format(k, v))  # .format sostituisce alle {} il valore che gli abbiamo passato

    def len(self):
        return len(self.avl)

    def get_frequency(self,p):
        return p.value()[0]

    def get_total(self,p):
        return p.value()[1]

    def occurrences(self):
        """Restituisce la somma delle frequenze di tutti gli elementi presenti nella mappa"""
        if self.len() == 0:
            raise Exception("Il dataset è vuoto")
        occorrenze = 0
        for p in self.avl.preorder():
            occorrenze += self.get_frequency(p)
            #occorrenze += e.value()[0]
        return occorrenze

    def average(self):
        """Restituisce la media dei valori di tutte le occorrenze presenti nel dataset"""
        #media dei valori = totale dei valori / totale delle occorrenze
        if self.len() == 0:
            raise Exception("La media è 0 perché il dataset è vuoto")

        complessivo = 0
        for p in self.avl.preorder():
            complessivo += self.get_total(p)
        return complessivo/self.occurrences()

    def median(self):
        """ se il numero n di dati è dispari la mediana corrisponde al valore centrale,
            ovvero al valore che occupa la posizione ( n + 1 ) / 2.

            se il numero  n di dati è pari, la mediana è stimata utilizzando i due valori
            che occupano le posizioni ( n / 2 ) e ( ( n / 2 ) + 1 )
            :return: il valore della mediana"""
        # entries = 0
        # for key in self.avl.keys():
        #     entries += self.avl[key][0]
        # freq = 0
        # for node in self.avl.inorder():
        #     freq += node.value()[0]
        #     if freq >= entries / 2:
        #         return node.key()
        return self.percentile(50)

    def percentile(self, j=20):
        entries = 0
        for key in self.avl.keys():
            entries += self.avl[key][0]
        freq = 0
        for node in self.avl.inorder():
            freq += node.value()[0]
            if freq/entries >= j/100:
                return node.key()

    def mostFrequent(self, j):
        lista = {}
        for e in self.avl.preorder():
            print(e.key())
            lista[e.key()] = e.value()[0]
        lista = sorted(lista, key=lista.getitem, reverse=True)
        return lista[0:j]


if __name__ == "__main__":
    stat = Statistics("data_set.txt")
    for e in stat.avl.preorder():
        print(e.key(), " ", e.value())

    print(stat.occurrences())
    print(stat.average())

    # stat.add(4, 5)
    # for e in stat.avl.preorder():
    #     print(e.key(), " ", e.value())
