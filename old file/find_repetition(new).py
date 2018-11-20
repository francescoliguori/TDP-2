'''Supponete di avere la directory dir contenente n file, alcuni dei quali potrebbero essere
copie con nomi diversi. Fornire la funzione find_repetition(dir) che, presa in input la
directory dir, restituisce la lista dei file replicati. La funzione proposta deve avere
complessità lineare nel numero dei file esaminati.'''
import os
import hashlib
import _md5
import sys
import filecmp
import stat
import io
def find_repetition(dir):
    unique = []
    list=[]
    for filename in os.listdir(dir):

        filepath=dir+filename
        if os.path.isfile(filepath):
            file=open(filepath, 'rb')
            filehash = hashlib.md5(file.read()).hexdigest()  #modificato qui
            file.close()
        if filehash not in unique:
            unique.append(filehash)
        else:
            list.append(filename)
    return list

